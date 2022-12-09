#!/usr/bin/env python3

import string

total = 0
lowercase = dict(zip(string.ascii_lowercase, range(1,27)))
uppercase = dict(zip(string.ascii_uppercase, range(27,53)))
lines = []
matching_letters = []

with open("input", "r") as file:
    for line in file:
        lines.append(line.rstrip())

for i in range(0,len(lines),3):
    for x in range(len(lines[i])):
        for y in range(len(lines[i+1])):
            for z in range(len(lines[i+2])):
                if (lines[i][x] == lines[i+1][y] and \
                    lines[i][x] == lines[i+2][z] and \
                    lines[i+1][y] == lines[i+2][z]):
                    matching_letters.append(lines[i][x])
    unique = []
    for x in matching_letters:
        if x not in unique:
            unique.append(x)

    for x in unique:
        for key,value in lowercase.items():
            if (key == x):
                total += value
        for key,value in uppercase.items():
            if (key == x):
                total += value
    matching_letters.clear()
    print(f"Answer: {total}")
