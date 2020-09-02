"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from operator import itemgetter
import numbers
with open('texts.csv', 'r') as file_:
    reader_ = csv.reader(file_)
    texts = list(reader_)

with open('calls.csv', 'r') as file_:
    reader_ = csv.reader(file_)
    calls = list(reader_)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

data_ = []
data_.extend(texts)
data_.extend(calls)


def getNumbers(all_numbers):
    numbers = []
    for row in all_numbers:
        numbers.append(row[0])
        numbers.append(row[1])
    return numbers


numbers = getNumbers(data_)
numbers = set(numbers)


def get_total_time(calls, number):
    total_time = 0
    for call in calls:
        if number in call:
            total_time += int(call[-1])
    return total_time


total_times = {}
for number in numbers:
    total_times[number] = get_total_time(calls, number)

print(
    f"{max(total_times, key=total_times.get)} spent the longest time, {total_times[max(total_times, key=total_times.get)]} seconds, on the phone during September 2016.")
