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


# PART A

# loop all over file calls
# if from_number start_with (080):
#    if to_number start_with '(': add code to area_code_list
#    elif to_number contains space " ": add 4 first digits to mobile_code
#    else: do nothing

# sort final_list asc


def numbers_code_called_by_people_in_bangalore(call_list):
    code_list = []
    for call in call_list:
        from_num = call[0]
        to_num = call[1]
        if from_num[0:5] == "(080)":
            if to_num[0] == "(" and to_num[1:4] not in code_list:
                code_list.append(to_num[1:4])
            elif to_num[5] == " " and to_num[0:4] not in code_list:
                code_list.append(to_num[0:4])
            else:
                pass
    return code_list


def test_part_a():
    code_list_called_by_people_in_bangalore = numbers_code_called_by_people_in_bangalore(calls)
    print("The numbers called by people in Bangalore have codes:")
    code_list_called_by_people_in_bangalore.sort()
    for code in code_list_called_by_people_in_bangalore:
        print(code)


# part B
def percent_call_from_fixed_line_to_fixed_line_in_bangalore(call_list):
    calls_made_by_fixed_line_in_bangalore = 0
    calls_between_fixed_lines_in_bangalore = 0
    for call in call_list:
        from_num = call[0]
        to_num = call[1]
        if from_num[0:5] == "(080)":
            calls_made_by_fixed_line_in_bangalore += 1
            if to_num[0:5] == "(080)":
                calls_between_fixed_lines_in_bangalore += 1

    return (calls_between_fixed_lines_in_bangalore / calls_made_by_fixed_line_in_bangalore)*100 \
        if calls_made_by_fixed_line_in_bangalore > 0 else 0


def test_part_b():
    percentage = round(percent_call_from_fixed_line_to_fixed_line_in_bangalore(calls), 2)
    print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


print("-------------- PART A ---------------")
test_part_a()
print("-------------- PART B ---------------")
test_part_b()
