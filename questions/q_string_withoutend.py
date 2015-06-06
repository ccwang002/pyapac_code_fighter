'''Question string_withoutend: (copyright -> CodingBat)

Description
-----------

Given a string, return a version without the first and last char, so "Hello"
yields "ell". The string length will be at least 2.


Examples
--------

answer('Hello') -> 'ell'
answer('java') -> 'av'
answer('coding') -> 'odin'

'''

def answer(str_in):
    return ''


def test_answer_ex1():
    str_in = 'here is a test to know'
    assert answer(str_in) == 'ere is a test to kno'


def test_answer_ex2():
    str_in = 'hw'
    assert answer(str_in) == 'hw'

def test_answer_ex3():
    str_in = 'k'
    assert answer(str_in) == 'k'

def test_answer_ex4():
    str_in = 'PyCon APAC 2015'
    assert answer(str_in) == 'yCon APAC 201'
