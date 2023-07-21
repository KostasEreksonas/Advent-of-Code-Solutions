#!/usr/bin/env python3
def directions(filename,floor,position):
    with open(filename) as file:
        line = file.read()
        for char in line:
            while floor != -1:
                print(f"Floor: {floor}")
                if char == '(':
                    floor += 1
                    position += 1
                elif char == ')':
                    floor -= 1
                    position += 1
            break;
    return position

print(directions("input",0,1))
