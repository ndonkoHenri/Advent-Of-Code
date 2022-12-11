# https://adventofcode.com/2022/day/10#part1

# read the file containing the input and store its contents
with open("input.txt", "rt") as f:
    str_input = f.read()

# split the input at line end
list_input = str_input.splitlines()

X = [1]
cycles = 1
signal_strength = set()
is_breakpoint = lambda e: e in [20, 60, 100, 140, 180, 220]


def check_cycles(c):
    if is_breakpoint(c):
        signal_strength.add(sum(X) * c)


# iterate over our input while checking if the cycles figure in the breakpoints | 20, 60 etc
for i in [w.split(" ") for w in list_input]:
    cycles += 1
    check_cycles(cycles)
    if i[0] == "addx":
        X.append(int(i[1]))
        cycles += 1
    check_cycles(cycles)

# print out the answer/signal strength
print(f"Signal Strength= {sum(signal_strength)}")
