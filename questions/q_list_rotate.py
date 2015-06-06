'''Question list_rotate: (copyright -> CodingBat)

Description
-----------

Given an array of arbitray size, return an array with the elements "rotated
left".


Examples
--------

    >>> answer([1, 2, 3])
    [2, 3, 1]

    >>> answer(['a', 'b', 'c', 'd'])
    ['b', 'c', 'd', 'a']

'''

def answer(list_in):
    return []


def test_answer_ex1():
    ref = [4, 99, 3]
    ans = answer([3, 4, 99])
    assert len(ans) == len(ref)
    for a, r in zip(ans, ref):
        assert a == r


def test_answer_ex2():
    ref = ['b', 'c', 'a', 'zz']
    ans = answer(['zz', 'b', 'c', 'a'])
    assert len(ans) == len(ref)
    for a, r in zip(ans, ref):
        assert a == r


def test_empty():
    ans = answer([])
    assert len(ans) == 0
    assert not ans
