import string   # necessary to avoid hard-coding the lower and upper case letters

# read the file containing the input and store its contents
with open("input.txt", "rt") as f:
    str_input = f.read()

# split the input at line end
list_input = str_input.splitlines()

# a parser to get the priority of the found common letter
case_parser = {
    "lowercase": {
        x: priority for priority, x in enumerate(string.ascii_lowercase, 1)
    },
    "uppercase": {
        y: priority for priority, y in enumerate(string.ascii_uppercase, 27)
    }
}

# variable to keep track of the total
total_priorities = 0

for rucksack in list_input:
    # separate into the two compartments
    c1, c2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
    # get the common letter from the two compartments
    common = [i for i in c1 if i in c2][0]
    # parse the common letter using case_parser
    priority_common = case_parser["lowercase" if common.islower() else 'uppercase'][common]
    # add the priority of the common letter to our total
    total_priorities += priority_common

# print out the final answer (the sum of all the obtained priorities)
print(f"Sum of Priorities(ANSWER): {total_priorities}")
