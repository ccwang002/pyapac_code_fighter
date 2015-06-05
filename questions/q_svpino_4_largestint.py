'''Question svpino 4: Form the largest number


Description
-----------

Write a function that given a list of non negative integers, arranges them
such that they form the largest possible number.


Examples
--------

    >>> answer([50, 2, 1, 9])
    95021

    >>> answer([5, 5, 6, 6])
    6655

    >>> answer([95, 2, 7])
    9572

'''

def answer(given_ints):
    combined_int = int(''.join(map(str, given_ints)))
    return combined_int


def test_example_50219():
    assert answer([50, 2, 1, 9]) == 95021


def test_example_5566():
    assert answer([5, 5, 6, 6]) == 6655


def test_example_9527():
    assert answer([95, 2, 7]) == 9572
    assert answer([9, 527]) == 9527
    assert answer([9, 5, 27]) == 9527
    assert answer([9, 5, 2, 7]) == 9752


def test_zeros():
    assert answer([5, 2, 0, 1, 314, 5, 56, 6]) == 65655314210
    assert answer([689, 40, 5, 84, 60, 9]) == 98468960540
