''' listing 6: pi_mp.py
Multiprocessing based code to estimate the value of PI
using monte carlo sampling 
Ref: http://math.fullerton.edu/mathews/n2003/montecarlopimod.html
Uses workers: 
http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
Adapted from Original Source: https://gist.github.com/amitsaha/2036026
'''

import random
import multiprocessing
from multiprocessing import Pool

def calculate_pi(n):
    np = multiprocessing.cpu_count()
    print ('You have {0:1d} CPUs'.format(np))
    # iterable with a list of points to generate in each worker
    # each worker process gets n/np number of points to calculate Pi from
    part_count=[n//np for i in range(np)]
    #Create the worker pool
    # http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
    pool = Pool(processes=np)
    # parallel map
    finalCount=pool.map(monte_carlo_pi_part, part_count)
    pi=sum(finalCount)/(n*1.0)*4
    print (pi)


def monte_carlo_pi_part(n):
    
    count = 0
    for i in range(n):
        x=random.random()
        y=random.random()
        
        # if it is within the unit circle
        if x*x + y*y <= 1:
            count=count+1
        
    #return
    return count



