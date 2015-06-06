'''Question foo: It's time to foo

Description
---------------
In this question, you are asked to implement a function to tell
if given inputs pycon years


Examples
-------------
answer('pycon2015')   # 2015
answer('Pycon2015')   # 2015
answer('PyCon2015')   # 2015
answer('PyCon 2015')   # 2015
answer('PyCon  2015')   # 2015
answer('PYCON  2015')   # 2015
answer('pycoN  2015')   # None

'''
from datetime import datetime

def answer(data):
    return ''

def test_answer_pycon1():
    data = "pycon2015"
    assert answer(data)  == 2015

def test_answer_pycon2():
    data = "pycon2014"
    assert answer(data)  == 2014

def test_answer_pycon3():
    data = "pycoN2014"
    assert answer(data)  == None

def test_answer_pycon4():
    data = "PYCON2014"
    assert answer(data)  == 2014

def test_answer_pycon5():
    data = "Pycon 2014"
    assert answer(data)  == 2014

def test_answer_pycon5():
    data = " FakePycon 2014"
    assert answer(data)  == None

def test_answer_pycon5():
    data = " fake Pycon 2014 "
    assert answer(data)  == None
