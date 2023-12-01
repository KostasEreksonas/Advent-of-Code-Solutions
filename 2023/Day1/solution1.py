#!/usr/bin/env python3

def digit_sum(filename):
    with open(filename, 'r') as f:
        lines = f.read().split()
    result = 0
    numbers = []
    for line in lines:
        digits = []
        for digit in line:
            if digit.isdigit():
                digits.append(digit)
        numbers.append(int(str(digits[0]) + str(digits[-1])))
    for number in numbers:
        result += number
    return result

def main():
    print(digit_sum("input"))

if __name__ == "__main__":
    main()
