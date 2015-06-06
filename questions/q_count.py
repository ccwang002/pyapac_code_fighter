'''Question foo: It's time to foo

Description
---------------
count python 


Examples
-------------
answer(["python", "ruby", "python", "c", "c","java", "php"])    == 2

'''
from datetime import datetime

def answer(data):
    return ''

def test_answer_pycon1():
    data = ["python", "ruby", "python", "c", "c","java", "php"]
    assert answer(data)  == 2


def test_answer_pycon1():
    data = ["python", "ruby", "python", "c", "c","java", "php","python","java"]
    assert answer(data)  == 3

