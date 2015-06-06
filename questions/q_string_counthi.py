'''Question string_counthi: xxx

Description
-----------

We always say hi to each other.
Now given a sentence, find how many hi in there.


Examples
--------

    >>> answer('hi, i am mark here hi.')
    2

    >>> answer('Hitori needs hard work. HI')
    1

'''

def answer(sentence):

    return 0

def test_answer_1():
    text = 'hi, i am mark. And hi, i am alfred. He is liang!, hi.'
    assert(answer(text)==3)
    
def test_answer_2():
    text = 'hi, there. Hell Hidra!'
    assert(answer(text)==1)
    
def test_answer_3():
    text = 'hi, hihihi, hi, HI, Hi, hIIIHI.HIHiHi.'
    assert(answer(text)==4)