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

def answer(*foos):
    """Tell if all dates have same day."""
    return True  # or False

def test_answer_foo():
    assert answer('foo')

def test_answer_bar():
    assert not answer('bar')

def test_hidden_large_list_foos():
    assert answer('foo', 'foobar')
    assert not answer('foo', 'foobar', 'fo')
