#pragma once
#include <complex>
#include <iostream>
#include <span>
#include <vector>

template<typename T>
void fwht_inplace(std::span<T> vec)
{
	std::vector<T> transformed(vec.size());

	size_t h = 1;
	while(h < vec.size())
	{
#pragma omp parallel for shared(vec,transformed) firstprivate(h)
		for(size_t i = 0; i < vec.size(); i += 2*h) {
			std::transform(vec.begin() + i, vec.begin() + i + h,
					vec.begin() + i + h, transformed.begin() + i,
					std::plus<T>());
			std::transform(vec.begin() + i , vec.begin() + i + h,
					vec.begin() + i + h, transformed.begin() + i + h,
					std::minus<T>());
		}
		std::copy(transformed.begin(), transformed.end(), vec.begin());
		h *= 2;
	}
}
