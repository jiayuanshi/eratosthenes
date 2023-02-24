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

        # The primes tail will be kept both as a set and as a sorted list
        primes_tail_lst = range(first,nmax+1,2)
        primes_tail_set = set(primes_tail_lst)

        # Now do the actual sieve
        while first <= round(math.sqrt(primes_tail_lst[-1])):
            # Move the first leftover prime from the set to the head list
            first = primes_tail_lst[0]
            primes_tail_set.remove(first)  # remove it from the set
            primes_head.append(first) # and store it in the head list

            # Now, remove from the primes tail all non-primes.  For us to be able
            # to break as soon as a key is not found, it's crucial that the tail
            # list is always sorted.
            for next_candidate in primes_tail_lst:
                try:
                    primes_tail_set.remove(first * next_candidate)
                except KeyError:
                    break

            # Build a new sorted tail list with the leftover keys
            primes_tail_lst = list(primes_tail_set)
            primes_tail_lst.sort()

        all_primes = primes_head + primes_tail_lst

    return all_primes
