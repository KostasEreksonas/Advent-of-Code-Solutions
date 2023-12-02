#!/usr/bin/env python3

keys = {"red":12, "green":13, "blue":14}

count = {"red":0, "green":0, "blue":0}

with open ("input", 'r') as f:
    games = f.read().split("\n")

for game in games:
    values = game.split(":")[1].split(";")
    print(values)
