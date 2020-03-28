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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


# get caller_number and receiver_number lists from calls file
def caller_n_receiver_list(call_list):
    caller_list = []
    call_receiver_list = []
    for call in call_list:
        caller_list.append(call[0])
        call_receiver_list.append(call[1])
    return caller_list, call_receiver_list


# get sender_number and receiver_number lists from texts file
def sender_n_receiver_list(sms_list):
    sender_list = []
    sms_receiver_list = []
    for sms in sms_list:
        sender_list.append(sms[0])
        sms_receiver_list.append(sms[1])
    return sender_list, sms_receiver_list


# get possible telemarketers' numbers
def telemarketers_numbers(call_list, sms_list):
    call_caller_list, call_receiver_list = caller_n_receiver_list(call_list)
    sms_sender_list, sms_receiver_list = sender_n_receiver_list(sms_list)
    telemarketers_numbers_list = []
    for caller in call_caller_list:
        if (
            caller not in call_receiver_list and
            caller not in sms_sender_list and
            caller not in sms_receiver_list and
            caller not in telemarketers_numbers_list
        ):
            telemarketers_numbers_list.append(caller)
    return telemarketers_numbers_list


def test():
    telemarketers_numbers_list = telemarketers_numbers(calls, texts)
    telemarketers_numbers_list.sort()
    print("These numbers could be telemarketers: ")
    for number in telemarketers_numbers_list:
        print(number)


test()
