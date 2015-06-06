r'''Question Add Braces: Find indent block and add braces

Description
-----------

Iblis hates braces, so he want to write proram without braces as block.

However, the C language uses braces to describe blocks.

He needs a tool to find the block with indents and modify it with braces.

Every indents are just 4 space charactors.

Examples
--------

>>> s = """
... for (int i=0; i<10; i++):
...     printf('Hello world\n');
... """
>>> print(answer(s))
for (int i=0; i<10; i++) {
    printf('Hello world\n');
    }
>>> s ="""
... if (i>1):
...     if (i>1):
...         printf('Hello world\n');
... """
>>> print(answer(s))
if (i>1) {
    if (i>1) {
        printf('Hello world\n');
        }
    }

'''

def answer(text):
    "answer here"
    return text_


def test_answer():
    s = """
for (int i=0; i<10; i++):
    printf('Hello world\n');
"""
    assert answer(s) == '''
for (int i=0; i<10; i++) {
    printf('Hello world\n');
    }
'''

def test_two_deepth():
    s ="""
if (i>1):
    if (i>1):
        printf('Hello world\n');
"""
    assert answer(s)) == '''
if (i>1) {
    if (i>1) {
        printf('Hello world\n');
        }
    }
'''
