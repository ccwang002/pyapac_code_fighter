'''Question foo: It's time to foo

Description
---------------
In this question foo, you are asked to implement a function to tell
if given inputs datetime object 


Examples
-------------
answer("2015-06-05")   # datetime(2015,6,5)
answer("2015-06-06")   # datetime(2015,6,6)
answer("2015-06-07")   # datetime(2015,6,7)

'''
from datetime import datetime

def answer(datetime_string):
    """ yyyy-mm-dd to datetime object """
    return ''

def test_answer_now():
    now = datetime.now()
    assert answer(now.strftime('%y-%m-%d'))  == datetime.strptime(now.strftime('%y-%m-%d'), "%y-%m-%d")

