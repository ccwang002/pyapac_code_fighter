'''Question svpino 2: Concat two list

Description
-----------

Write a function that combines two lists by alternatingly taking elements.

Note: ignore the NaN comparison. We don't test that :)

(From the blog post "5 prog. problems every software engineer" should be
able to solve in less than 1 hour.)


Examples
--------

    >>> answer(['a', 'b', 'c'], [1, 2, 3])
    ['a', 1, 'b', 2, 'c', 3]

    >>> answer(['f', 'o', 'o'], ['b'])
    ['f', 'b', 'o', 'o']

'''

def answer(list1, list2):
    """Alternatively take elements from two lists."""
    return list1 + list2


def _all_equal(ref, ans):
    if len(ref) != len(ans):
        return False
    return all(r == a for r, a in zip(ref, ans))


def test_answer_ex1():
    l_abc = list('abc')
    l_123 = list(range(1, 4))
    assert _all_equal(answer(l_abc, l_123), ['a', 1, 'b', 2, 'c', 3])


def test_answer_ex2():
    foo = list('foo')
    b = ['b']
    assert _all_equal(answer(foo, b), ['f', 'b', 'o', 'o'])


def test_custom_class_by_val():
    class Foo:
        def __init__(self, x):
            self.x = x

        def __eq__(self, other):
            if isinstance(other, Foo):
                return self.x == other.x
            else:
                return False

    list_a = list(map(Foo, [1, 3]))
    list_b = list(map(Foo, [2, 4]))
    assert _all_equal(
        answer(list_a, list_b),
        [list_a[0], list_b[0], list_a[1], list_b[1]]
    )


def test_custom_class_by_obj():
    class Foo:
        def __init__(self, x):
            self.x = x

    list_a = list(map(Foo, [1, 3]))
    list_b = list(map(Foo, [2, 4]))
    assert _all_equal(
        answer(list_a, list_b),
        [list_a[0], list_b[0], list_a[1], list_b[1]]
    )
