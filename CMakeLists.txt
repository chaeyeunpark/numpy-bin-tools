cmake_minimum_required(VERSION 3.9)

project(numpy-bin-tools)

if(NOT CMAKE_BUILD_TYPE)
	set(CMAKE_BUILD_TYPE Release)
endif()

set(CMAKE_CXX_STANDARD 20)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Werror")

include(FetchContent)
FetchContent_Declare(pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG        v2.10.1
)
FetchContent_MakeAvailable(pybind11)

find_package(OpenMP REQUIRED)

pybind11_add_module(_numpy_bin_tools cpp_src/binding.cpp)
target_link_libraries(_numpy_bin_tools PRIVATE OpenMP::OpenMP_CXX)
