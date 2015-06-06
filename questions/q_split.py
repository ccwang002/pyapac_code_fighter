'''Question foo: It's time to foo

Description
---------------
In this question, you are asked to implement a function to tell
if given inputs pycon years


Examples
-------------
input """

PyConTW 
Microsoft's Azure Workshop is launching! Get gifts by finishing missions:https://t.co/Zt9RRIh5Z2 #pyconapac http://t.co/ueLX3rD7RA
Takanori Suzuki 
きゃーーー @atelierhide さーーーーん #pyconapac #pydatatokyo http://t.co/CmSkSK9UsM
Yoshi 
RT @szuluyang: Promoting Gandi at #pyconapac2015 @Gandi_TW http://t.co/NJR0ZHxYG2
Yung-Yu Chen 
PyConTW 
A beautiful day begins with Keynote 3, delivered by Robert Bradshaw! Day 2 Hackpad:https://t.co/qNqVWVzuWc #pyconapac http://t.co/D1WxUZoHar
Indeed aliens are more interesting #marsface #pyconapac @atelierhide http://t.co/agritdzG4W
"""

output
["""Microsoft's Azure Workshop is launching! Get gifts by finishing missions:https://t.co/Zt9RRIh5Z2 #pyconapac http://t.co/ueLX3rD7RA
Takanori Suzuki""",
"""A beautiful day begins with Keynote 3, delivered by Robert Bradshaw! Day 2 Hackpad:https://t.co/qNqVWVzuWc #pyconapac http://t.co/D1WxUZoHar
Indeed aliens are more interesting #marsface #pyconapac @atelierhide http://t.co/agritdzG4W"""
]

'''
from datetime import datetime

def answer(data):
    return ''

def test_answer_pycon1():
    data = """PyConTW 
    Arnaud Bergeron's fantastic Keynote had finished. Now, it's Job Fair! Come and join Show Time at 4F. #pyconapac2015 http://t.co/xuYekfDtQA
    PyConTW 
    Refresh time! Excellent talks, Cloud Panel and Job Fair are gonna to catch your eyes! #pyconapac http://t.co/u0xzllPpVk
    PyConTW 
    Microsoft's Azure Workshop is launching! Get gifts by finishing missions:https://t.co/Zt9RRIh5Z2 #pyconapac http://t.co/ueLX3rD7RA
    Takanori Suzuki 
    きゃーーー @atelierhide さーーーーん #pyconapac #pydatatokyo http://t.co/CmSkSK9UsM
    Yoshi 
    RT @szuluyang: Promoting Gandi at #pyconapac2015 @Gandi_TW http://t.co/NJR0ZHxYG2
    Yung-Yu Chen 
    PyConTW 
    A beautiful day begins with Keynote 3, delivered by Robert Bradshaw! Day 2 Hackpad:https://t.co/qNqVWVzuWc #pyconapac http://t.co/D1WxUZoHar
    Indeed aliens are more interesting #marsface #pyconapac @atelierhide http://t.co/agritdzG4W
    Eva YANG 
    Promoting Gandi at #pyconapac2015 @Gandi_TW http://t.co/NJR0ZHxYG2
    Yung-Yu Chen 
    #marsface #pyconapac #microsoft #azure http://t.co/1U74to6V2M
    PyConTW 
    Besides taking notes on Hackpad (https://t.co/qNqVWVzuWc), you can also chat with others on Gitter (https://t.co/xJmLYjsL65) #pyconapac2015"""

    result = [v.strip() for v in data.split('Pycon') if v.strip()]
    assert sorted(answer(data)) == sorted(result)


