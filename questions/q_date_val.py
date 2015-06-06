'''Question date_val: Date validation

Description
-----------
Tell if the given year, month, day is valid.


Examples
--------

    >>> answer(6, 50)
    False

    >>> answer(2, 29)
    True

    >>> answer(2, 30)
    False

'''
def answer(year, month, day):
    return True

def test_jun_50():
    assert not answer(2015, 6, 50)

def test_feb_28():
    assert answer(2015, 2, 28)

def test_feb_30():
    assert not answer(2015, 2, 30)

def test_all_months_zero_or_neg():
    for mm in range(1, 13):
        assert not answer(mm, 0)
        assert not answer(mm, -1)

def test_end_of_all_months():
    end_dates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for mm, date in enumerate(end_dates, 1):
        assert answer(mm, date)
        assert answer(mm, date - 1)
        assert answer(mm, 1)
        assert not answer(mm, date + 1)
