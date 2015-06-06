'''Question prime_sum: (copyright -> CodingBat)

Description
-----------

Find the sum of all positive prime numbers less than n.
n is between 10^6 and 10^7 


Examples
--------

    >>> answer(2) -> 0
    >>> answer(3) -> 2
    >>> answer(10) -> 17
    >>> answer(100) -> 1060

'''

def answer(n):
    return 0

def _xprime(n):
    table = [0] * n
    one = [1] * n
    s = 0
    for p in range(2, n):
        if table[p]==0:
            s+=p
            table[p*p:n:p] = one[p*p:n:p]
    print(s)
    
        
def test_answer_ex1():
    n_in = 2000000
    assert 142913828922 is answer(n_in)


def test_answer_ex2():
    n_in = 5000000
    assert 838596693108 == answer(n_in)

