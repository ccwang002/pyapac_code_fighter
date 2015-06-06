r'''Question Colorful Print: Create a new print function

Description
-----------

Create a new print function, which can color its output with member function of `print` object.

The new `print` object might be a function, or a instance of the new "Print" class.

Whatever, just see the example below.

All of the "color name - color value" mapping (i.e, a function) has already defined.

>>> Colors['red']("my text")
'[31mmy text[m'


Examples
--------

>>> print = answer()
>>> print(123)
123
>>> print.red(123)
[31m123[m
>>> print.blue(123)
[34m123[m
>>> print.blue.red(123)
[34m[31m123[m[m

'''

def answer():
    class Print:
        "Your answer here"
    return Print()


def dump_output(program):
    from contextlib import redirect_stdout
    from io import StringIO

    with redirect_stdout(StringIO()) as buff:
        exec(program)
        return buff.getvalue()


def test_orig():
    print = answer()
    assert(dump_output(print('qwer')) == 'qwer')

def test_reverse():
    print = answer()
    assert(dump_output(print.reverse('qwer')) == '[7mqwer[m')

def test_dim_red_bold():
    print = answer()
    assert(dump_output(print.dim.red.bold('qwer')) == '[2m[31m[1mqwer[m[m[m')


Colors = {
    'reset':              "[0m{}[m".format,
    'bold':               "[1m{}[m".format,
    'bright':             "[1m{}[m".format,
    'dim':                "[2m{}[m".format,
    'underscore':         "[4m{}[m".format,
    'underlined':         "[4m{}[m".format,
    'blink':              "[5m{}[m".format,
    'reverse':            "[7m{}[m".format,
    'hidden':             "[8m{}[m".format,
    'black':              "[30m{}[m".format,
    'red':                "[31m{}[m".format,
    'green':              "[32m{}[m".format,
    'yellow':             "[33m{}[m".format,
    'blue':               "[34m{}[m".format,
    'magenta':            "[35m{}[m".format,
    'purple':             "[35m{}[m".format,
    'aqua':               "[36m{}[m".format,
    'cyan':               "[36m{}[m".format,
    'white':              "[37m{}[m".format,
    'bgblack':            "[40m{}[m".format,
    'bgred':              "[41m{}[m".format,
    'bggreen':            "[42m{}[m".format,
    'bgyellow':           "[43m{}[m".format,
    'bgblue':             "[44m{}[m".format,
    'bgmagenta':          "[45m{}[m".format,
    'bgpurple':           "[45m{}[m".format,
    'bgaqua':             "[46m{}[m".format,
    'bgcyan':             "[46m{}[m".format,
    'bgwhite':            "[47m{}[m".format,
    }
