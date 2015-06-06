'''Question foo: It's time to foo

Description
---------------
http://adon988.logdown.com/posts/248475-2015-programming-languages-rankings-came-out
sort programming-languages rankings

Examples
-------------
input: [
    {"name":"python", "rating":2.613},
    {"name":"c", "rating":16.703},
    {"name":"java", "rating":15.52},
    {"name":"perl", "rating":2.256},
]
output:
["c", "java", "python", "perl"]
'''

def answer(datetime_string):
    return ''

def test_answer_now():
    data = [
        {"name":"python", "rating":2.613},
        {"name":"c", "rating":16.703},
        {"name":"ruby", "rating":1.13},
        {"name":"java", "rating":15.52},
        {"name":"perl", "rating":2.256},
    ]

    result = sorted(data, key=lambda v:v['rating'])
    result.reverse()
    result = [v['name'] for v in result]
    assert answer(result)  == datetime.strptime(now.strftime('%c'), "%c")

