#!/usr/bin/env python3

def house_count(filename,x,y):
    path = [[0,0]]
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                coordinates = []
                if char == '^':
                    y += 1
                elif char == 'v':
                    y -= 1
                elif char == '>':
                    x += 1
                elif char == '<':
                    x -= 1
                coordinates.append(x)
                coordinates.append(y)
                path.append(coordinates)
    return path

def unique(arr):
    uniq = []
    [uniq.append(x) for x in arr if x not in uniq]
    return uniq

def main():
    arr = house_count('input',0,0)
    print(len(unique(arr)))

if __name__ == "__main__":
    main()
