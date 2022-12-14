# https://adventofcode.com/2022/day/12#part1

# read the file containing the input and store its contents
with open("input.txt", "rt") as f:
    str_input = f.read()

# split the input at line end
list_input = str_input.split('\n\n')


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


indices = []

# iterate over each pair, and if the left is less than right, then the order is correct -- store the value in 'indices'
for idx, pair in enumerate(list_input, 1):
    left, right = list(map(eval, pair.split("\n")))
    fix_mixed_types(left, right)

    if left < right:
        print(f"- Compare {left} vs {right}")
        print('\t- Left side || right order')
        indices.append(idx)
    else:
        print('\t- Right side || wrong order')

# print out the answer to the question
print(f"\nSum of Indices={sum(indices)}")
