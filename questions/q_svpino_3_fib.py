'''Question svpino 3: Fibanacci

Description
-----------

Write a function that computes the list of the first 100 Fibonacci numbers.
By definition, the first two numbers in the Fibonacci sequence are 0 and 1,
and each subsequent number is the sum of the previous two. As an example,
here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and
34.

(From the blog post "5 prog. problems every software engineer" should be
able to solve in less than 1 hour.)


Examples
--------

    >>> answer(0)
    0

    >>> answer(1)
    1

    >>> answer(2)
    1

    >>> list(map(answer, range(3, 11)))
    [2, 3, 5, 8, 13, 21, 34, 55]

    >>> answer(5) + answer(6) == answer(7)
    True

'''
from nose.tools import timed as _timed


def answer(n):
    """Implement the fibonacci function."""
    return n


def test_init_fib():
    first_ten = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    ans = list(map(answer, range(11)))
    assert len(ans) == len(first_ten)
    assert all(a == ref for a, ref in zip(ans, first_ten))


def test_higher_fib():
    next_ten = [
        89, 144, 233, 377, 610,
        987, 1597, 2584, 4181, 6765
    ]
    ans = list(map(answer, range(11, 21)))
    assert len(ans) == len(next_ten)
    assert all(a == ref for a, ref in zip(ans, next_ten))


@_timed(.5)
def test_super_large_fib():
    fib_95 = 31940434634990099905
    assert answer(95) == fib_95
