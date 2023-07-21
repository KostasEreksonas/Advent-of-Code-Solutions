#!/usr/bin/env python3

def wrapper(num1, num2, num3):
    arr = [num1,num2,num3]
    arr.remove(max(arr))
    return 2*(arr[0]+arr[1])

def ribbon(filename,total):
    with open(filename, 'r') as file:
        for line in file:
            dimensions = line.strip('\n').split('x')
            wrap = wrapper(int(dimensions[0]),int(dimensions[1]),int(dimensions[2]))
            total += int(dimensions[0])*int(dimensions[1])*int(dimensions[2]) + wrap
    return total

print(f"A total of {ribbon('input',0)} square feet of ribbon is needed.")
