#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include <cstdlib>

pybind11::array_t<uint32_t> to_bin_array(unsigned int N, uint64_t conf)
{
	namespace py = pybind11;
	py::array_t<uint32_t> res(N);
	py::buffer_info res_buf = res.request();
	uint32_t *res_ptr = static_cast<uint32_t*>(res_buf.ptr);

	for(unsigned int i = 0; i < N; i++)
	{
		res_ptr[i] = (conf >> i) & 1;
	}

	return res;
}
