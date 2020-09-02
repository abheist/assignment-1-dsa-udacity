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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
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
all_mobile_numbers = numbers

print(f"There are {len(numbers)} different telephone numbers in the records.")
