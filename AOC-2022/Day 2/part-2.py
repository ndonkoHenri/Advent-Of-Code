# read the file containing the input and store its contents
with open("input.txt", "rt") as f:
    str_input = f.read()

# split the input at line end
list_input = str_input.splitlines()

# create a list containing the predictions and recommendations of the strategy guide
strategy_guide = [i.split(' ') for i in list_input]

# dictionary used to parse the shape and the round outcome
my_parser = {
    "shape": {"A": 1, "B": 2, "C": 3},
    "round_outcome": {"lost": 0, "draw": 3, "won": 6}
}

# variable to keep track of our score
my_score = 0

for round_number, outcome in enumerate(strategy_guide, 1):
    # The first column is what your opponent is going to play :: The second column is what you are recommended to play
    opponent, round_end = outcome

    # Note: Z = need to win || Y = need to draw || X = need to loose

    if round_end == "Z":
        my_score += my_parser["shape"]["B" if opponent == "A" else "C" if opponent == "B" else "A"] + \
                    my_parser["round_outcome"]["won"]
        print(f"Round {round_number} | WON")
    elif round_end == "Y":
        my_score += my_parser["shape"][opponent] + my_parser["round_outcome"]["draw"]
        print(f"Round {round_number} | DRAW")
    elif round_end == "X":
        my_score += my_parser["shape"]["C" if opponent == "A" else "A" if opponent == "B" else "B"] + \
                    my_parser["round_outcome"]["lost"]
        print(f"Round {round_number} | LOST")


# print out your total score
print(f"\nTotal n° of rounds = {round_number}\nTotal Score = {my_score}")
