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


def bangalore_calls(calls):
    calls_from_bangalore = []
    for call in calls:
        if call[0].startswith("(080)"):
            calls_from_bangalore.append(call)
    return calls_from_bangalore


def bangalore_(bangalore):
    print("The numbers called by people in Bangalore have codes:")
    numbers_to_ = []
    for number in bangalore:
        if number[1].startswith("("):
            numbers_to_.append(number[1][1:number[1].find(")")])
        if number[1][:1] in ["7", "8", "9"]:
            numbers_to_.append(number[1][:4])
    return sorted(set(numbers_to_))


def area_calls(bangalore):
    area = []
    for call in calls:
        if call[0].startswith("(080)") and call[1].startswith("(080)"):
            area.append(call)
    print(
        f"{str(len(area)/len(bangalore)*100)[:5]} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


bangalore = bangalore_calls(calls)
bangalore_ = bangalore_(bangalore)

for i in bangalore_:
    print(i)
print()

area_calls(bangalore)
