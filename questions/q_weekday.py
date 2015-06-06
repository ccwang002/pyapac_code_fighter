'''Question foo: It's time to foo

Description
---------------
In this question foo, you are asked to implement a function to tell
if given inputs all begin with 'foo'


Examples
-------------
answer('foo')   # True
answer('bar')   # False
answer('foobar', 'foobaz')   # True
'''
from datetime import datetime

def answer(datetime_obj):
    """
        get week from  datetime_obj
        example:
            answer(datetime(2015,06,06)) == 6
    """
    return ''

def test_answer_now():
    now = datetime.now()
    assert answer(now)  == now.weekday() + 1


def test_answer_now():
    now = datetime(2014,1,1)
    assert answer(now)  == now.weekday() + 1



def test_answer_now():
    now = datetime(2014, 4,1)
    assert answer(now)  == now.weekday() + 1
