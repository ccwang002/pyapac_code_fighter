'''Question list::Rotate (copyright -> CodingBat)

Description
-----------


Given an array of arbitray size, return an array with the elements "rotated left". 


Examples
--------

    >>> answer([1, 2, 3]) -> [2, 3, 1]
    >>> answer(['a', 'b', 'c', 'd']) -> ['b', 'c', 'd', 'a']

'''

def answer(list_in):

    return []



def test_answer_ex1():
    l_in = [4, 99, 3]
    assert answer(l_in) == [99, 3, 4]


def test_answer_ex2():
    l_in = ['b', 'c', 'a', 'zz']
    assert answer(l_in) == ['c', 'a', 'zz', 'b']

