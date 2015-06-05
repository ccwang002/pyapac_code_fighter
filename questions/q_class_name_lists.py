'''Question class_name_lists: What's wrong? (Debug)

Description
-----------

Find the bug in the `answer` function.

This answer function is designed to help teacher Julia to manage 

the students' names in different classes she teachs.

We assume that all student are of unique names.

Input
-----
student_dist (Dictionary): a dictionary maps student name to the class number.
    {"Tom":1, "Mary":2} --> Tom is in class 1 and Mary is in class 2.

Return
------
names_lists (List): a list of lists where the first list contains all student names
                    in class 1, the second one contains all student names in class 2
                    , so on and so forth.
    ex: [["Tom"], ["Mary"]]


Examples
--------

    >>> answer({"Tom":1, "Mary":2, "Jerry":1, "Jack":3})
    [["Tom", "Jerry"], ["Mary"], ["Jack"]]

'''

def answer(mapping):
	num_of_classes = max(mapping.values())
	names_lists = [[]] * num_of_classes
	for name, class_no in mapping.items():
		names_lists[class_no].append(name)
	return names_lists

def test_four_classes():
	assert answer({"Tom":1, "Dboy":1, "c3h3":2, "Liang2":3, "Yen":4, "Wush":2, "Ning":4}) == [["Tom", "Daniel"], ["c3h3", "Wush"], ["Liang2"], ["Yen"]]

def test_empty_classes():
	assert answer({"c3h3":1, "Wush":4}) == [["c3h3"], [], [], ["Wush"]]

