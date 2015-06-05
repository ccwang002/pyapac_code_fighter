'''Question bad_default: What's wrong?

Description
-----------

Find the bug in the `answer` function.

The bug-free answer should insert all elements in the `values` argument 

into an empty list and return it every time when answer function is 

being called.


Examples
--------

    >>> answer([1, 2, 3])
    [1, 2, 3]

    >>> answer(('a', 'b', 'c'))
    ['a', 'b', 'c']

'''
def answer(values, result_list = []):
	for val in values:
		result_list.append(val)
	return result_list

def test_answer_list():
	answer([1])
	try:
		result = answer(['a', 'b', 'c']) 
		assert result == ['a', 'b', 'c']
	except:
		print("Expecting: ['a', 'b', 'c']")
		print("Get: {result}".format(result = result))
		raise AssertionError()

def test_answer_tuple():
	answer(['a'])
	try:
		result = answer((1, 2, 3)) 
		assert result == [1, 2, 3]
	except:
		print("Expecting: [1, 2, 3]")
		print("Get: {result}".format(result = result))
		raise AssertionError()

def test_answer_string():
	answer([1])
	try:
		result = answer(['Pycon'])
		assert result == ['P', 'y', 'C', 'o', 'n']
	except:
		print("Expecting: ['P', 'y', 'C', 'o', 'n']")
		print("Get: {result}".format(result = result))
		raise AssertionError()
