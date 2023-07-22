#!/usr/bin/env python3

def find_pairs(line):
    for i in range(len(line) - 3):
        if line[i:i+2] in line[i+2:]:
            return True
    return False

def repeat_letters(line):
    for i in range(len(line) -2):
        if line[i] == line[i+2]:
            return True
    return False

def nice_or_naughty(line):
    if find_pairs(line) == True and repeat_letters(line) == True:
        return 'nice'

def main():
    nice_count = 0
    with open ('input', 'r') as file:
        for line in file:
            if nice_or_naughty(line) == 'nice':
                nice_count += 1
    print(f"Nice string count: {nice_count}")

if __name__ == "__main__":
    main()
