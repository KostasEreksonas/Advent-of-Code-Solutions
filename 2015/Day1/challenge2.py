#!/usr/bin/env python3
def directions(filename,floor,position):
    with open(filename) as file:
        line = file.read()
        for char in line:
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
            position += 1
            if floor == -1:
                break;
    return position

print(f"Santa first enters the basement at position: {directions('input',0,0)}")
