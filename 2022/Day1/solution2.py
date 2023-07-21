#!/usr/bin/env python3

first = 0
second = 0
third = 0

with open("input.txt", "r") as file:
    count = 0
    for line in file:
        if (line != '\n'):
            num = line.strip()
            count += int(num)
        else:
            if (count > first):
                third = second
                second = first
                first = count
            elif (count < first and count > second):
                third = second
                second = count
            elif (count < second and count > third):
                third = count
            count = 0

sum = first + second + third
print(f"First highest number of calories is: {first}")
print(f"Second highest number of calories is: {second}")
print(f"Third highest number of calories is: {third}")
print(f"Total calories carried by top three elves: {sum}")
