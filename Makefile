clean:
	rm -rf ./numpy_bin_tools/*.cpython-*.so ./*.egg-info ./build
	find . -name "__pycache__" -exec rm -r {} +


