#!/usr/bin/env python3

def word_to_num(filename):
    with open(filename, 'r') as f:
        lines = f.read().split()
    numbers = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    newarray = []
    for line in lines:
        for key in numbers:
            newline = line.replace(key, key[0]+numbers[key]+key[-1])
            line = newline
        newarray.append(line)
    return newarray

def digit_sum(filename):
    lines = word_to_num(filename)
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
