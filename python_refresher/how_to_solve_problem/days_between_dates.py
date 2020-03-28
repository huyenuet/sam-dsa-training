# final step
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


# step 4
def days_in_month(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        if is_leap_year(year):
            return 29
        return 28
    return 30


# step 1: create next_day
def next_day(year, month, day):
    """assume that each month has 30 days"""
    if day < days_in_month(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month+1, 1
        else:
            return year+1, 1, 1


# step 1.5: helper function to check if date1 is before date2
def date_is_before(year1, month1, date1, year2, month2, date2):
    """Returning True if y-m-d 1 is before y-m-d 2. Otherwise, return False"""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return date1 < date2
    return False


# step 2: define days_between_dates to give approximate answers using next_day procedure
def days_between_dates(year1, month1, date1, year2, month2, date2):
    assert date_is_before(year1, month1, date1, year2, month2, date2)
    days = 0
    while date_is_before(year1, month1, date1, year2, month2, date2):
        days += 1
        year1, month1, date1 = next_day(year1, month1, date1)
    return days


def test():
    assert next_day(2019, 1, 1) == (2019, 1, 2)
    assert next_day(2019, 1, 30) == (2019, 1, 31)
    assert next_day(2019, 1, 31) == (2019, 2, 1)
    assert next_day(2019, 4, 29) == (2019, 4, 30)
    assert next_day(2019, 2, 28) == (2019, 3, 1)
    assert next_day(2019, 12, 31) == (2020, 1, 1)
    assert days_between_dates(2013, 1, 24, 2013, 6, 29) == 156
    assert days_between_dates(2013, 1, 1, 2014, 1, 1) == 365
    assert days_between_dates(2012, 1, 1, 2013, 1, 1) == 366
    assert is_leap_year(2012)
    assert is_leap_year(1996)
    assert not is_leap_year(2013)
    print(days_between_dates(2020, 2, 2, 2020, 3, 27)/7)
    print("test finished!")


test()
