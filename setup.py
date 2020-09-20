from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Monte Carlo Pi Approximation',
    ext_modules=cythonize("montecarlo_pi.py"),
    zip_safe=False,
)
