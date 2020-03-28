"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from datetime import datetime, timedelta

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def days_in_month(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        if is_leap_year(year):
            return 29
        return 28
    return 30


def time_spent_on_each_call(start_timestamp, duration, year, month):
    """
    Return duration in seconds of a call which is within a period (year-month)
    """
    start_timestamp = datetime.strptime(start_timestamp, "%d-%m-%Y %H:%M:%S")
    if start_timestamp.year != year:
        return 0
    if start_timestamp.month != month:
        return 0

    duration = int(duration)
    if start_timestamp.day < days_in_month(year, month):
        return duration

    end_timestamp = start_timestamp + timedelta(seconds=duration)
    final_date_of_period = datetime(year, month, days_in_month(year, month), 23, 59, 59)
    if end_timestamp <= final_date_of_period:
        return duration
    else:
        return (final_date_of_period - start_timestamp).seconds


def phone_number_and_total_call_time(call_list, year, month):
    num_n_spent_time_list = {}
    for call in call_list:
        on_call_time = time_spent_on_each_call(call[2], call[3], year, month)

        for i in range(2):
            if call[i] not in num_n_spent_time_list:
                # add [number phone, on_call_time into num_n_spent_time_list
                num_n_spent_time_list[call[i]] = on_call_time
            else:
                # add on_call_time to existed number phone in num_n_spent_time_list
                num_n_spent_time_list[call[i]] += on_call_time
    return num_n_spent_time_list


def longest_on_call_time_phone_number_in_period(call_list, year, month):
    longest_on_call_time = 0
    phone_number = None
    phone_number_spent_time_list = phone_number_and_total_call_time(call_list, year, month)
    for key in phone_number_spent_time_list:
        if longest_on_call_time < phone_number_spent_time_list[key]:
            longest_on_call_time = phone_number_spent_time_list[key]
            phone_number = key
    return phone_number, longest_on_call_time


def test():
    phone_number, total_time = longest_on_call_time_phone_number_in_period(calls, year=2016, month=9)
    print(f"{phone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.")


test()
