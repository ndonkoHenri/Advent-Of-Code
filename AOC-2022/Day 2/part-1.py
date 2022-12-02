# read the file containing the input and store its contents
with open("input.txt", "rt") as f:
    str_input = f.read()

# split the input at line end
list_input = str_input.splitlines()

# create a list containing the predictions and recommendations of the strategy guide
strategy_guide = [i.split(' ') for i in list_input]

# dictionary used to parse the shape and the round outcome
my_parser = {
    "shape": {"X": 1, "Y": 2, "Z": 3},
    "round_outcome": {"lost": 0, "draw": 3, "won": 6}
}

# variable to keep track of our score
my_score = 0

for round_number, outcome in enumerate(strategy_guide, 1):
    # The first column is what your opponent is going to play :: The second column is what you are recommended to play
    opponent, me = outcome
    my_shape = my_parser["shape"][me]
    # when I win the round
    if (me == "X" and opponent == "C") or (me == "Y" and opponent == "A") or (me == "Z" and opponent == "B"):
        my_score += my_shape + my_parser["round_outcome"]["won"]
        print(f"Round {round_number} | WON")
    # when there is draw
    elif (me == "X" and opponent == "A") or (me == "Y" and opponent == "B") or (me == "Z" and opponent == "C"):
        my_score += my_shape + my_parser["round_outcome"]["draw"]
        print(f"Round {round_number} | DRAW")
    # when I loose the round
    else:
        my_score += my_shape + my_parser["round_outcome"]["lost"]
        print(f"Round {round_number} | LOST")

# print out your total score
print(f"\nTotal n° of rounds = {round_number}\nTotal Score = {my_score}")
