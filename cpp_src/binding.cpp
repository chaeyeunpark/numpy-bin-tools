#include "fwht.hpp"
#include "to_bin_array.hpp"

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include <complex>
#include <iostream>
#include <span>

namespace py = pybind11;

template <typename T>
auto fwht_bind(py::array_t<T> arr) -> py::array_t<T> {
	if(arr.ndim() != 1)
	{
		throw std::invalid_argument("Array must be one dimensional.");
	}

	py::buffer_info arr_buf = arr.request();

	T* arr_ptr = static_cast<T*>(arr_buf.ptr);
	size_t arr_size = arr_buf.shape[0];

	if (std::popcount(arr_size) != 1) {
		throw std::invalid_argument("Size of the input array must be a power of 2.");
	}

	py::array_t<T> res(arr_size);
	py::buffer_info res_buf = res.request();
	T* res_ptr = static_cast<T*>(res_buf.ptr);

	std::copy(arr_ptr, arr_ptr + arr_size, res_ptr);

	fwht_inplace(std::span(static_cast<T*>(res_ptr), arr_size));

	const T factor = std::sqrt(arr_size);
#pragma omp parallel for
	for(size_t i = 0; i < arr_size; i++) {
		res_ptr[i] /= factor;
	}
	return res;
};

PYBIND11_MODULE(_numpy_bin_tools, m) {
	m.def("walsh_hadamard", fwht_bind<float>,
			"A function calculating the fast Walsh-Hadamard transformation.");

	m.def("walsh_hadamard", fwht_bind<double>,
			"A function calculating the fast Walsh-Hadamard transformation.");

	m.def("walsh_hadamard", fwht_bind<std::complex<float>>,
			"A function calculating the fast Walsh-Hadamard transformation.");

	m.def("walsh_hadamard", fwht_bind<std::complex<double>>,
			"A function calculating the fast Walsh-Hadamard transformation.");

	m.def("to_bin_array", to_bin_array, "A function convert a 64 bit (unsigned) integer to bit array.");
}
