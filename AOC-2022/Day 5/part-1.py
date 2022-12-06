# https://adventofcode.com/2022/day/5#part1

import re
from typing import Dict, List

# read the file containing the input and store its contents
with open("input.txt", "rt") as f:
    str_input = f.read()

# split the input at line end
list_input = str_input.splitlines()

# copied the values in the input, and arranged them into a dict of lists for easy removal/addition
my_parser: Dict[str, List] = {
    '1': ['W', 'M', 'L', 'F'],
    '2': ['B', 'Z', 'V', 'M', 'F'],
    '3': ['H', 'V', 'R', 'S', 'L', 'Q'],
    '4': ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J'],
    '5': ['L', 'S', 'W'],
    '6': ['F', 'W', 'P', 'M', 'R', 'J', 'W'],
    '7': ['J', 'Q', 'C', 'P', 'N', 'R', 'F'],
    '8': ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B'],
    '9': ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']
}

# use regular expressions to extract the three numbers in each line of our input
instructions = [re.findall(r"\d+", i) for i in list_input[10:]]

# get the three extracted numbers
for x in instructions:
    how_many = int(x[0])    # how many items are to be moved?
    move_from = x[1]    # move these items from
    move_to = x[2]      # move these items to
    
    # move the values accordingly
    for y in range(how_many):
        last_value = my_parser[move_from].pop()
        my_parser[move_to].append(last_value)

# print out the ANSWER (last value of each list)
for z in my_parser.values():
    print(z[-1], end="")

