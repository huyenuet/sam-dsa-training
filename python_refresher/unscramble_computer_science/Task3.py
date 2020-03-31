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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def get_phone_number_code(phone_num):
    if phone_num[:3] == '140':
        return '140'
    if phone_num[0] == "(":
        return phone_num[1:].split(")")[0]
    if phone_num[0] in ('7', '8', '9'):
        return phone_num[:4]
    return


# PART A
def get_phone_number_code_receive_call_from_people_in_bangalore(call_list):
    code_set = set()
    for call in call_list:
        from_phone_number_code = get_phone_number_code(call[0])
        to_phone_number_code = get_phone_number_code(call[1])
        if from_phone_number_code == "080":
            code_set.add(to_phone_number_code)
    return code_set


def test_part_a():
    code_list_called_by_people_in_bangalore = get_phone_number_code_receive_call_from_people_in_bangalore(calls)
    print("The numbers called by people in Bangalore have codes:")
    sorted_code_list = sorted(code_list_called_by_people_in_bangalore)
    for code in sorted_code_list:
        print(code)


# PART B
def get_percent_call_from_fixed_line_to_fixed_line_in_bangalore(call_list):
    calls_made_by_fixed_line_in_bangalore = 0
    calls_between_fixed_lines_in_bangalore = 0
    for call in call_list:
        from_phone_number_code = get_phone_number_code(call[0])
        to_phone_number_code = get_phone_number_code(call[1])
        if from_phone_number_code == "080":
            calls_made_by_fixed_line_in_bangalore += 1
            if to_phone_number_code == "080":
                calls_between_fixed_lines_in_bangalore += 1

    return (calls_between_fixed_lines_in_bangalore / calls_made_by_fixed_line_in_bangalore) * 100 \
        if calls_made_by_fixed_line_in_bangalore > 0 else 0


def test_part_b():
    percentage = round(get_percent_call_from_fixed_line_to_fixed_line_in_bangalore(calls), 2)
    print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


print("-------------- PART A ---------------")
test_part_a()
print("-------------- PART B ---------------")
test_part_b()

# expected output
# -------------- PART A ---------------
# The numbers called by people in Bangalore have codes:
# 022
# 040
# 04344
# 044
# 04546
# 0471
# 080
# 0821
# 7406
# 7795
# 7813
# 7829
# 8151
# 8152
# 8301
# 8431
# 8714
# 9008
# 9019
# 9035
# 9036
# 9241
# 9242
# 9341
# 9342
# 9343
# 9400
# 9448
# 9449
# 9526
# 9656
# 9738
# 9740
# 9741
# 9742
# 9844
# 9845
# 9900
# 9961
# -------------- PART B ---------------
# 24.81 percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.
