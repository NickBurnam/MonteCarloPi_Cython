Setup Guide for Monte Carlo Pi Python to C conversion with Cython

Reference: https://cython.readthedocs.io/en/latest/src/quickstart/install.html
	   https://cython.readthedocs.io/en/latest/src/quickstart/build.html 

Install Cython with:
$ pip3 install Cython

montecarlo_pi.py is to be converted to C
montecarlo_pi_python3.py is the same code but we will run it in python3

In the setup.py, specify the python file you wish to convert - ext_modules=cythonize("file_name.py")
Then run the command in the directory with the files: 

$ python3 setup.py build_ext --inplace

This will generate the C code and a module that can be imported and ran just like any python module

In montecarlo_pi_main.py import the C module montecarlo_pi, and the python module montecarlo_pi_python3
Run both Pi approximations and compare the execution time.
