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


# get caller_number and receiver_number sets from calls file
def get_call_callers_and_receivers(call_list):
    callers = set()
    receivers = set()
    for call in call_list:
        callers.add(call[0])
        receivers.add(call[1])
    return callers, receivers


# get sender_number and receiver_number sets from texts file
def get_sms_senders_and_receivers(sms_list):
    sender_set = set()
    receivers = set()
    for sms in sms_list:
        sender_set.add(sms[0])
        receivers.add(sms[1])
    return sender_set, receivers


# get possible telemarketers' numbers
def find_telemarketers_numbers(call_list, sms_list):
    call_callers, call_receivers = get_call_callers_and_receivers(call_list)
    sms_sender_set, sms_receivers = get_sms_senders_and_receivers(sms_list)
    return call_callers - (call_receivers | sms_sender_set | sms_receivers)


def test():
    telemarketers_numbers_set = find_telemarketers_numbers(calls, texts)
    telemarketers_numbers_list = sorted(telemarketers_numbers_set)
    print("These numbers could be telemarketers: ")
    for number in telemarketers_numbers_list:
        print(number)


test()

# expected result:
# 43 telemarketers
# (022)37572285
# (022)65548497
# (022)68535788
# (022)69042431
# (040)30429041
# (044)22020822
# (0471)2171438
# (0471)6579079
# (080)20383942
# (080)25820765
# (080)31606520
# (080)40362016
# (080)60463379
# (080)60998034
# (080)62963633
# (080)64015211
# (080)69887826
# (0821)3257740
# 1400481538
# 1401747654
# 1402316533
# 1403072432
# 1403579926
# 1404073047
# 1404368883
# 1404787681
# 1407539117
# 1408371942
# 1408409918
# 1408672243
# 1409421631
# 1409668775
# 1409994233
# 74064 66270
# 78291 94593
# 87144 55014
# 90351 90193
# 92414 69419
# 94495 03761
# 97404 30456
# 97407 84573
# 97442 45192
# 99617 25274
