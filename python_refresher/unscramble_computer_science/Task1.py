"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def get_diff_phone_numbers(num_list):
    distinct_num_set = set()
    for num in num_list:
        distinct_num_set.add(num[0])
        distinct_num_set.add(num[1])
    return distinct_num_set


def test():
    distinct_num_set = get_diff_phone_numbers(calls) | get_diff_phone_numbers(texts)
    distinct_number_count = len(distinct_num_set)
    print(f"There are {distinct_number_count} different telephone numbers in the records.")


test()

# expected output
# There are 570 different telephone numbers in the records.
