'''Question logic_love7: (copyright -> CodingBat)


Description
-----------


The number 7 is a truly great lucky number. Given two int values, a and b,
return True if either one is 7. Or if their sum or difference is 6.


Examples
--------


'''

def answer(a, b):

    return True


def test_answer_ex1():
    test = (1, 8)
    assert answer(*test)

def test_answer_ex2():
    test = (7, 8)
    assert answer(*test)

def test_answer_ex3():
    test = (-4, 11)
    assert answer(*test)

def test_answer_ex4():
    test = (99, 91)
    assert not answer(*test)

def test_answer_ex5():
    test = (1, 3)
    assert not answer(*test)
