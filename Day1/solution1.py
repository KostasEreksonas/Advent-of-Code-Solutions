#!/usr/bin/env python3

highest = 0
with open("input.txt", "r") as file:
    count = 0
    for line in file:
        if (line != '\n'):
            num = line.strip()
            count += int(num)
        else:
            if (count > highest):
                highest = count
            count = 0

print(f"Highest number of calories is: {highest}")
