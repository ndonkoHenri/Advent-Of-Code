# read the file containing the input and store its contents
with open("input.txt", "rt") as f:
    str_input = f.read()

# split the input at line end
list_input = str_input.splitlines()

# split each line into two sections
sections = [r.split(',') for r in list_input]

# variable to keep track of the total number of assignment pairs
total_assignment_pairs = 0

for i, j in sections:
    # split i and j at '-' and convert them to sets to easily obtain their common values(intersections)
    i, j = i.split("-"), j.split("-")
    # +1 in the range() is necessary because the 'stop' value of the range is excluded
    set_i, set_j = set(range(int(i[0]), int(i[1]) + 1)), set(range(int(j[0]), int(j[1]) + 1))
    # get the intersection of the two sets
    intersection = set_i.intersection(set_j)
    # if there is an intersection between them, increment the total by 1
    if intersection:
        total_assignment_pairs += 1

# print out the Total pairs (ANSWER to the question)
print(f"{total_assignment_pairs=}")
