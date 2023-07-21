#!/usr/bin/env python3

overlap = 0

with open("input", "r") as file:
    for line in file:
        ranges = line.strip("\n").split(",")
        first_bounds = ranges[0].split("-")
        second_bounds = ranges[1].split("-")
        int_first_bounds = int(first_bounds[0])
        int_second_bounds = int(second_bounds[0])
        if (int(second_bounds[0]) >= int(first_bounds[0]) and \
            int(second_bounds[1]) <= int(first_bounds[1]) or \
            int(first_bounds[0]) >= int(second_bounds[0]) and \
            int(first_bounds[1]) <= int(second_bounds[1])):
            overlap += 1
print(f"Overlap: {overlap}")
