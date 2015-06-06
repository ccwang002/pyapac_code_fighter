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
    ref = [1, 5, 6]
    ans = answer(a, b)
    assert len(ref) == len(ans)
    for r, a in zip(ref, ans):
        assert r == a

def test_answer_tuple():
    a = ['c', 'd', 'e', 'f', 'g', 'k']
    b = ['c', 'd', 'e']
    ref = ['f', 'g', 'k']
    ans = answer(a, b)
    assert len(ref) == len(ans)
    for r, a in zip(ref, ans):
        assert r == a
