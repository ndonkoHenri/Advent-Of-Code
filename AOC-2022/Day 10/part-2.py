# https://adventofcode.com/2022/day/10#part2
import numpy as np

# read the file containing the input and store its contents
with open("test-input.txt", "rt") as f:
    str_input = f.read()

# split the input at line end
list_input = str_input.splitlines()

X = 1
cycles = 1
sprite = np.array([0, 1, 2])

points = ["#", "#", "#"]
points.extend(["*"] * 237)

crt_pos = 0
crt_row = []


def crt_draw():
    """
    It prints out the crt's image (40 characters per line)
    """
    for x in range(40, 241, 40):
        print("".join(crt_row)[x - 40:x])


def reset_crt_pos():
    """
    If the current position is 40, reset it to 0
    """
    global crt_pos
    if crt_pos == 40:
        crt_pos = 0


# iterate over our input
for i in [w.split(" ") for w in list_input]:
    print(f"Sprite Position: {list(sprite)}")
    cycles += 1
    print(f"Starting cycle {cycles}: begin executing {' '.join(i)}")
    print(f"During cycle {cycles}: CRT draws pixel in position {crt_pos}")
    crt_row.append("#" if crt_pos in sprite else '.')
    crt_pos += 1
    reset_crt_pos()
    print(f"Current CRT row: {''.join(crt_row)}")

    if i[0] == "addx":
        ax = int(i[1])      # get the value next to 'addx'
        X += ax             # increment the register
        cycles += 1         # increment the actual number of cycles
        print(f"During cycle {cycles}: CRT draws pixel in position {crt_pos}")
        crt_row.append("#" if crt_pos in sprite else '.')   # if crt_pos is in the sprite's values, append # else .
        crt_pos += 1
        reset_crt_pos()
        print(f"Current CRT row: {''.join(crt_row)}")

        sprite += np.array([ax, ax, ax])        # modify the sprite's position

    print(f"End of cycle {cycles}: finish executing {' '.join(i)} (Register X is now {X})\n")

crt_draw()
