#!/usr/bin/env python3

def check_vowels(line):
    count = 0
    for char in line:
        if char in 'aeiou':
            count += 1
    return count

def double_letters(line):
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            return True
    return False

def forbidden_strings(line):
    if 'ab' not in line and 'cd' not in line and 'pq' not in line and 'xy' not in line:
        return True
    else:
        return False

def nice_or_naughty(line):
    if check_vowels(line) >= 3 and double_letters(line) == True and forbidden_strings(line) == True:
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
