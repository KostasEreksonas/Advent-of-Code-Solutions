#!/usr/bin/env python3

import string

total = 0

lowercase = dict(zip(string.ascii_lowercase, range(1,27)))
uppercase = dict(zip(string.ascii_uppercase, range(27,53)))

with open("input", "r") as file:
    for line in file:
        matching_letters = []
        letterCount = len(line.rstrip())
        string1 = line[0:letterCount//2]
        string2 = line[letterCount//2:letterCount]
        for i in range(letterCount//2):
            for j in range(letterCount//2):
                if (string1[i] == string2[j]):
                    matching_letters.append(string1[i])
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

print(f"Answer: {total}")
