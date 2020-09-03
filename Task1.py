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

data_ = set()


def getNumbers(all_numbers):
    for row in all_numbers:
        data_.add(row[0])
        data_.add(row[1])


getNumbers(texts)
getNumbers(calls)

print(f"There are {len(data_)} different telephone numbers in the records.")
