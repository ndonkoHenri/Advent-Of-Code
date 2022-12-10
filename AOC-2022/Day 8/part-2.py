# https://adventofcode.com/2022/day/8#part2

# read the file containing the input and store its contents
with open("input.txt", "rt") as f:
    str_input = f.read()
list_input = str_input.splitlines()


scenic_scores = []

# Checking if the tree is visible from the left, right, top, or bottom byt iterating on each line, and each tree
for line_index, i in enumerate(list_input[1:-1]):
    for tree_index, tree_height in enumerate(i[1:-1], 1):
        # to better understand the indexes I used, print out the values' ex: list_input[:line_index+1]

        # initialize the number of trees we've seen (zero at start)
        left, right, top, down = 0, 0, 0, 0

        # left
        for x in i[:tree_index][::-1]:  # this string/iterator is reversed to start from inside going outside
            left += 1   # add one because the tree is visible
            # break this loop if the height of the tree(x) is greater than or equal the height of the tree we are at
            if int(x) >= int(tree_height):
                break

        # right
        for y in i[tree_index + 1:]:
            right += 1   # add one because the tree is visible
            # break this loop if the height of the tree(y) is greater than or equal the height of the tree we are at
            if int(y) >= int(tree_height):
                break

        # top
        for z in list_input[:line_index + 1].__reversed__():
            top += 1   # add one because the tree is visible
            # break this loop if the height of the tree(z) is greater than or equal the height of the tree we are at
            if int(z[tree_index]) >= int(tree_height):
                break

        # down
        for d in list_input[line_index + 1 + 1:]:
            down += 1    # add one because the tree is visible
            # break this loop if the height of the tree(d) is greater than or equal the height of the tree we are at
            if int(d[tree_index]) >= int(tree_height):
                break

        # append the product of our results
        scenic_scores.append(top * left * down * right)

# print out the answer to the question - the maximum scenic score
print(f"ANSWER(Scenic Score)= {max(scenic_scores)}")
