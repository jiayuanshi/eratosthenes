# %%time

import sys
import math
import numpy as np

def find_primes(nmax):
    all_primes = []

    if nmax == 2: 
        all_primes = [2]
    else:
        primes_head = [2]
        first = 3
        primes_tail = np.arange(first,nmax+1,2)
        while first <= round(math.sqrt(primes_tail[-1])):
            first = primes_tail[0]
            primes_head.append(first)
            non_primes = first * primes_tail
            primes_tail = np.array([ n for n in primes_tail[1:]
                                    if n not in non_primes ])

    all_primes = primes_head + primes_tail.tolist()
    return all_primes
