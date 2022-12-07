#!/usr/bin/env python3

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
        for key, value in player.items():
            if (game[1] == key):
                player_val = value
        if (opponent_val == player_val):
            total += 3
        elif (opponent_val == "Rock" and player_val == "Paper"):
            total += 6
        elif (opponent_val == "Scissors" and player_val == "Rock"):
            total += 6
        elif (opponent_val == "Paper" and player_val == "Scissors"):
            total += 6
        if (player_val == "Rock"):
            total += 1
        elif (player_val == "Paper"):
            total += 2
        elif (player_val == "Scissors"):
            total += 3
    print(f"Total: {total}")
