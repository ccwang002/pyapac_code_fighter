'''Question foo: It's time to foo

Description
---------------
In this question foo, you are asked to implement a function to tell
if given inputs all begin with 'foo'


Examples
-------------
answer('Sat Jun  6 14:43:49 2015')   # datetime.datetime(2015, 6, 6, 14, 43, 49)
'''
from datetime import datetime

def answer(datetime_string):
    return ''

def test_answer_now():
    now = datetime.now()
    assert answer(now.strftime('%c'))  == datetime.strptime(now.strftime('%c'), "%c")

