'''Question Faster Sieve: Make this code faster

Description
-----------

There is a program coming from a movie "Ex Machinima" which define two functions to find the n-th prime.

It is too slow with bigger N. We have to make it faster; however, the code is not Pythonic...

Try to understand the code and modify it to let it faster. 


Examples
--------

(Since the program is not Pythonic, it is also no example here)

'''

from nose.tools import timed


def answer():

    def sieve(n):
        x = [1]*n
        x[1] = 0
        for i in range(2,n/2):
            j = 2*i
            while j < n:
                x[j] = 0
                j = j+1
        return x
    
    def prime(n, x):
        i = 1
        j = 1 
        while j <= n: 
            if x[i] == 1: 
                j = j+1 
            i = i+1 
        return i-1 
     
    return sieve, prime


@timed(10)
def test_speed_challenge():
    nth_prime = lambda n: primes(n-1, sieve(10))
    assert nth_prime(1) == 2

    nth_prime = lambda n: primes(n-1, sieve(100))
    assert nth_prime(5) == 11

    nth_prime = lambda n: primes(n-1, sieve(10000))
    assert nth_prime(301) == 1993

    nth_prime = lambda n: primes(n-1, sieve(10000))
    assert nth_prime(384) == 2657

    nth_prime = lambda n: primes(n-1, sieve(100000))
    assert nth_prime(1206) == 9781
