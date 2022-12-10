# https://adventofcode.com/2022/day/8#part1

# read the file containing the input and store its contents
with open("input.txt", "rt") as f:
    str_input = f.read()
list_input = str_input.splitlines()

trees_per_line = len(list_input[0])     # the number of tress found in the line (5 in test-input and 99 in input)

total = (trees_per_line * 2) + ((len(list_input) - 2) * 2)  # add all the already-visible trees (those on the outside)

# Checking if the tree is visible from the left, right, top, or bottom byt iterating on each line, and each tree
for line_index, i in enumerate(list_input[1:-1]):
    for tree_index, tree_height in enumerate(i[1:-1], 1):
        # to better understand the list comprehensions and the indexes I used,
        # print out the values' ex: list_input[:line_index+1]
        is_visible_left = all([False if int(x) >= int(tree_height) else True for x in i[:tree_index]])
        is_visible_right = all([False if int(y) >= int(tree_height) else True for y in i[tree_index + 1:]])
        is_visible_top = all(
            [False if int(z[tree_index]) >= int(tree_height) else True for z in list_input[:line_index+1]])
        is_visible_down = all(
            [False if int(z[tree_index]) >= int(tree_height) else True for z in list_input[line_index + 1 + 1:]])

        # the below comment is for debug purposes with the test data
        """print(
            tree_height,
            [is_visible_left, is_visible_right, is_visible_top, is_visible_down],
            (line_index, list_input[:line_index+1], list_input[line_index + 1 + 1:])
        )"""

        # if the tree is visible on one of the sides: either left, right, top, or bottom, increment the total
        if any([is_visible_left, is_visible_right, is_visible_top, is_visible_down]):
            total += 1

# print out the answer to the question
print(f"ANSWER= {total}")
