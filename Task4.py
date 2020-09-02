"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as file_:
    reader_ = csv.reader(file_)
    texts = list(reader_)

with open('calls.csv', 'r') as file_:
    reader_ = csv.reader(file_)
    calls = list(reader_)

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

telemarketers = [number[0] for number in calls]
telemarketers = set(telemarketers)


def texts_checks(texts, telemarketers):
    for number in texts:
        if number[0] in telemarketers:
            telemarketers.remove(number[0])
        if number[1] in telemarketers:
            telemarketers.remove(number[1])
    return telemarketers


def call_checks(calls, telemarketers):
    for number in calls:
        if number[1] in telemarketers:
            telemarketers.remove(number[1])
    return telemarketers


telemarketers = texts_checks(texts, telemarketers)
telemarketers = call_checks(calls, telemarketers)

print("These numbers could be telemarketers: ")
for number in sorted(telemarketers):
    print(number)
