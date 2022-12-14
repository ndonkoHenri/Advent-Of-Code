# https://adventofcode.com/2022/day/10#part1

# read the file containing the input and store its contents
with open("test-input.txt", "rt") as f:
    str_input = f.read()

# split the input at line end
list_input = str_input.split('\n\n')


def check_mixed_types(x: list, y: list, debug=False):
    print(f"- START: {x} VS {y}")
    for i in range(min(len(x), len(y))):

        if (isinstance(x[i], int) and isinstance(y[i], list)) or (isinstance(x[i], list) and isinstance(y[i], int)):
            if isinstance(x[i], int):
                x[i] = eval("[x[i]]")
            else:
                y[i] = eval("[y[i]]")

            # print("INT LIST = ",x[i]," ** ", y[i])

        elif isinstance(x[i], list) and isinstance(y[i], list):
            x[i], y[i] = check_mixed_types(x[i], y[i])

        if debug:
            print("\t", x[i], "\n\t", y[i], "\n")
            if isinstance(x[i], list) and isinstance(y[i], list):
                check_mixed_types(x[i], y[i], True)
    # print(f"- END: {x} VS {y}")
    return x, y


indices = []

for idx, pair in enumerate(list_input, 1):
    l1, l2 = list(map(eval, pair.split("\n")))
    # print(f"- Compare {l1} vs {l2}")
    # print(f"- {l1} VS {l2}")
    s1, s2 = check_mixed_types(l1, l2, True)
    print(f"- END: {s1} VS {s2}")
    print("\t\t", l1, l1 == s1, s1, l2, s2 == l2, s2)
    try:
        if s1 < s2:
            # print(f"- Compare {l1} vs {l2}")
            # print('\t- Left side || right order')
            indices.append(idx)
        # else:
        #     print('\t- Right side || wrong order')

    except TypeError as excep:
        print(f"- {l1} VS {l2}\n- {s1} VS {s2}")
        # print(f"{l1} VS {l2}")
        check_mixed_types(l1, l2, True)
        print(excep, "\n")

print(f"\n{indices=}\nSum of Indices={sum(indices)}")
