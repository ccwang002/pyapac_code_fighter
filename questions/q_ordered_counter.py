'''Question ordered_counter: Count maintains the order


Description
-----------

Count the occurence of the elements and maintain their order.

It's okay to return as a OrderedDict.

Examples
--------

    >>> answer('abbbbccdd')
    [('a', 1), ('b', 4), ('c', 2), ('d', 2)]

    >>> answer([5, 5, 6, 6, 9, 5, 2, 7, 6, 8, 9, 6, 0, 9])
    [(5, 3), (6, 4), (9, 3), (2, 1), (7, 1), (8, 1), (0, 1)]

'''
from collections import OrderedDict


def answer(seq):
    from collections import OrderedDict
    return OrderedDict.from_keys(set(seq))


def test_example_1():
    ref = OrderedDict([('a', 1), ('b', 4), ('c', 2), ('d', 2)])
    ans = OrderedDict(answer('abbbbccdd'))

    assert set(ref.keys()) == set(ans.keys())
    for (r_key, r_val), (a_key, a_val) in zip(ref.items(), ans.items()):
        assert r_key == a_key
        assert r_val == a_val


def test_example_2():
    ref = OrderedDict([
        (5, 3), (6, 4), (9, 3), (2, 1),
        (7, 1), (8, 1), (0, 1)
    ])
    ans = OrderedDict(answer(
        [5, 5, 6, 6, 9, 5, 2, 7, 6, 8, 9, 6, 0, 9]
    ))

    assert set(ref.keys()) == set(ans.keys())
    for (r_key, r_val), (a_key, a_val) in zip(ref.items(), ans.items()):
        assert r_key == a_key
        assert r_val == a_val

