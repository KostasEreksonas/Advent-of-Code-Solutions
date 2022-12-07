#!/usr/bin/env python3

#A,Y - Rock; B,X - Paper; C,Z - Scissors
# A beats Z
# B beats Y
# C beats X
# Y beats C
# X beats A
# Z beats B

count = 0
total = 0
opponent = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}

player = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

with open("input", "r") as file:
    for line in file:
        game = line.strip("\n").split(" ", 1)
        for key, value in opponent.items():
            if (game[0] == key):
                opponent_val = value
        if (game[1] == "X"):
            if (opponent_val == "Rock"):
                total += 3
            elif (opponent_val == "Scissors"):
                total += 2
            elif (opponent_val == "Paper"):
                total += 1
        if (game[1] == "Y"):
            if (opponent_val == "Rock"):
                total += 4
            elif (opponent_val == "Scissors"):
                total += 6
            elif (opponent_val == "Paper"):
                total += 5
        if (game[1] == "Z"):
            if (opponent_val == "Rock"):
                total += 8
            elif (opponent_val == "Scissors"):
                total += 7
            elif (opponent_val == "Paper"):
                total += 9
    print(f"Total: {total}")
