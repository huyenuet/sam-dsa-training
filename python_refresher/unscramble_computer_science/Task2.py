"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict
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


def get_duration_in_period(start_timestamp, duration, year, month):
    """
    Return duration in seconds which is within a period (year-month)
    """
    start_timestamp = datetime.strptime(start_timestamp, "%d-%m-%Y %H:%M:%S")
    if start_timestamp.year != year:
        return 0
    if start_timestamp.month != month:
        return 0
    return duration


def get_phone_number_and_total_call_time(call_list, year, month):
    """
    Return a dictionary with key = phone_number, value = total_call_time
    """
    number_and_spent_time = defaultdict(int)
    for call in call_list:
        duration = get_duration_in_period(call[2], int(call[3]), year, month)
        for i in range(2):
            number_and_spent_time[call[i]] += duration
    return number_and_spent_time


def get_phone_number_with_longest_call_time_in_period(call_list, year, month):
    """
    Return the phone number which spent longest time on calls
    """
    records = get_phone_number_and_total_call_time(call_list, year, month)
    return max(records.items(), key=lambda p: p[1])


def test():
    phone_number, total_time = get_phone_number_with_longest_call_time_in_period(calls, year=2016, month=9)
    print(f"{phone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.")


test()

# expected output:
# (080)33251027 spent the longest time, 90456 seconds, on the phone during September 2016.
