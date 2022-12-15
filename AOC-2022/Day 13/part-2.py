# https://adventofcode.com/2022/day/13#part2
from itertools import zip_longest

# read the file containing the input and store its contents
with open("input.txt", "rt") as f:
    str_input = f.read()

# split the input at line end
packets = str_input.split('\n\n')
packets = [j for pair in packets for j in list(map(eval, pair.split("\n")))]


def fix_mixed_types(x: list, y: list) -> None:
    """
    If the ith element of x is an integer and the ith element of y is a list, then the ith element of x is converted to
    a list. Similarly, if the ith element of x is a list and the ith element of y is an integer, then the ith element
    of y is converted to a list
    """
    for i in range(min(len(x), len(y))):
        if (isinstance(x[i], int) and isinstance(y[i], list)) or (isinstance(x[i], list) and isinstance(y[i], int)):
            if isinstance(x[i], int):
                x[i] = eval("[x[i]]")
            else:
                y[i] = eval("[y[i]]")

        if isinstance(x[i], list) and isinstance(y[i], list):
            fix_mixed_types(x[i], y[i])


def compare_even(iterator: list):
    """
    This is an even comparison: the first element the first element is compared to the second element,
    the third with the fourth, the fifth with the sixth, and so on.
    """
    global packets
    a = []
    for y, z in zip(iterator[0::2], iterator[1::2]):
        fix_mixed_types(y, z)
        if y < z:
            a.append(y)
            a.append(z)
        else:
            a.append(z)
            a.append(y)

    # set the packets to the newly created list
    packets = a

    # without this try-except, a TypeError will be raised by the sort() method
    # we then change the comparison method
    try:
        packets.sort()  # if this is successful, then we are sure to have correctly sorted the packets
    except TypeError:
        compare_odd(a)


def compare_odd(iterator: list):
    """
    This is an odd comparison: the first element is added to a new list (not sorted), and then the rest of the list
    is sorted by comparing the second element with the third, the fourth with the fifth, and so on.
    """
    global packets

    a = [iterator[0]]
    for y, z in zip_longest(iterator[1::2], iterator[2::2]):
        if y is not None and z is not None:
            fix_mixed_types(y, z)
            if y < z:
                a.append(y)
                a.append(z)
            else:
                a.append(z)
                a.append(y)
        # trying to append the last value in the pair, excluding None - ex: ([1,2], None)
        if y is None:
            a.append(z)
        elif z is None:
            a.append(y)

    # set the packets to the newly created list
    packets = a

    # without this try-except, a TypeError will be raised by the sort() method
    # we then change the comparison method
    try:
        packets.sort()  # if this is successful, then we are sure to have correctly sorted the packets
    except TypeError:
        compare_even(a)


# Sorting the list of packets.
compare_even(packets)

divider_packets = []

# Printing out the divider packets with length of one and their corresponding indices
for index, p in enumerate(packets, 1):
    if len(p) == 1:
        divider_packets.append((index, p))
        print(f"{index} -- -- {p}")

# print out the answer to the question
print(f"\n\nLOCATE THE INDICES OF TWO DIVIDER PACKETS INSIDE THE PRINTOUTS AND MULTIPLY THEM TO HAVE THE DECODER KEY!")
print("So: 113*208 = 23504")

# todo: find a way to easily extract the divider packets (index)
