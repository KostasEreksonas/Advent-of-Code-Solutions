#!/usr/bin/env python3

def house_count(filename,x,y,x1,y1):
    path_santa = [[0,0]]
    path_robot = [[0,0]]
    with open(filename, 'r') as file:
        for line in file:
            for i in range(len(line)):
                coordinates = []
                if i == 0 or i % 2 == 0:
                    if line[i] == '^':
                     y += 1
                    elif line[i] == 'v':
                        y -= 1
                    elif line[i] == '>':
                        x += 1
                    elif line[i] == '<':
                        x -= 1
                    coordinates.append(x)
                    coordinates.append(y)
                    path_santa.append(coordinates)
                elif i % 2 != 0 :
                    if line[i] == '^':
                        y1 += 1
                    elif line[i] == 'v':
                        y1 -= 1
                    elif line[i] == '>':
                        x1 += 1
                    elif line[i] == '<':
                        x1 -= 1
                    coordinates.append(x1)
                    coordinates.append(y1)
                    path_robot.append(coordinates)
    path = path_santa + path_robot
    return path

def unique(arr):
    uniq = []
    [uniq.append(x) for x in arr if x not in uniq]
    return uniq

def main():
    arr = house_count('input',0,0,0,0)
    print(len(unique(arr)))

if __name__ == "__main__":
    main()
