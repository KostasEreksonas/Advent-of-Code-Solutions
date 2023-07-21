#!/usr/bin/env python3

def smallest(num1, num2, num3):
    arr = [num1,num2,num3]
    return min(arr)

def paper(filename,total):
    with open(filename, 'r') as file:
        for line in file:
            dimensions = line.strip('\n').split('x')
            a1 = int(dimensions[0]) * int(dimensions[1])
            a2 = int(dimensions[1]) * int(dimensions[2])
            a3 = int(dimensions[2]) * int(dimensions[0])
            slack = smallest(a1,a2,a3)
            total += 2*(a1+a2+a3) + slack
    return total

print(f"A total of {paper('input',0)} square feet of wrapping paper is needed.")
