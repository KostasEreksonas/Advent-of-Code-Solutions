#!/usr/bin/env python3
def directions(filename,direction1,direction2):
    with open(filename) as file:
        line = file.read()
        for char in line:
            if char == '(':
                direction1 += 1
            elif char == ')':
                direction2 += 1
    return direction1 - direction2

print(directions("input",0,0))
