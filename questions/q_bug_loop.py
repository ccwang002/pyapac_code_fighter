'''Question bad_default: What's wrong? (Debug)

Description
-----------

Given list a, b

We'd like to remove item in a if item in b.

However, we are failed. 

Please help us to fix the bug.



Examples
--------

a = [1, 3, 4, 5, 6]
b = [3, 4]

Expected = [1, 5, 6]
What we got = [1, 4, 5, 6]

'''

def answer(list_a, list_b):
    for item in list_a:
        if item in list_b:
            list_a.remove(item)
    return list_a

def test_answer_list():
    a = [1, 3, 4, 5, 6]
    b = [3, 4]
    assert(answer(a, b) == [1,5,6] )

def test_answer_tuple():
    a = ['c','d','e','f', 'g', 'k']
    b = ['c','d','e']
    assert(answer(a, b) == ['f', 'g', 'k'])
