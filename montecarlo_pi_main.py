import timeit

print("Running x = 1000000000 iterations for each approximation")

print("Python converted to C t(s)",timeit.timeit(setup="import montecarlo_pi; x = 1000000000", stmt="montecarlo_pi.calculate_pi(x)", number=1))
print("Pure Python t(s): ",timeit.timeit(setup="import montecarlo_pi_python3; x = 1000000000", stmt="montecarlo_pi_python3.calculate_pi(x)", number=1))
