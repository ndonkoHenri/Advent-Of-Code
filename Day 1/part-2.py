# read the file containing the input and store its contents
with open("input.txt", "rt") as f:
    calories_str_input = f.read()

# split the string into a list
calories_list_input = calories_str_input.split("\n\n")

# variable to store the sum of each elves' calories
calories_sum = []

for cal in calories_list_input:
    # convert the string values to integers, sum up, and append to our list
    calories_sum.append(sum(map(int, [j for j in cal.split('\n') if j])))

# sort in descending order
y = sorted(calories_sum, reverse=True)
print(y[0] + y[1] + y[2])  # print out the sum of the first three values: ANSWER
