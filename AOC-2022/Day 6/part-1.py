# https://adventofcode.com/2022/day/6#part1
from collections import Counter

# read the file containing the input and store its contents
with open("input.txt", "rt") as f:
    datastream_buffer = f.read()

for idx, j in enumerate(datastream_buffer):
    # grab a serie of 4 characters
    four = datastream_buffer[idx:idx + 3 + 1]
    # this will count the number of times each character in the variable 'four' occurs
    count = Counter(four)

    # if the occurrence count of each the characters in the variable 'four' is 1
    if all([i == 1 for i in count.values()]):
        # print out the answer and break the loop
        print("ANSWER=", idx + 3 + 1)
        break
