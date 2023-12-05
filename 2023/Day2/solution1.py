#!/usr/bin/env python3

keys = {"red":12, "green":13, "blue":14}

count = {"red":0, "green":0, "blue":0}

with open ("input", 'r') as f:
    games = f.read().split("\n")

del games[-1]

for game in games:
    #g = game.split(": ")[-1].split("; ")[-1].split(", ")
    g = game.split(": ")
    ids = g[0].split()[-1]
    for x in range(len(g[1].split("; "))):
        print(g[1].split(", ")[x])
    #print(f"{game}, {type(game)}")
