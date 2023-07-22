#!/usr/bin/env python3

import hashlib

def _hash(key,num):
    while True:
        s = key+str(num)
        result = hashlib.md5(s.encode())
        if result.hexdigest()[:5] == '00000':
            break
        else:
            num += 1
    return num

def main():
    key = 'yzbqklnj'
    print(_hash(key,0))

if __name__ == "__main__":
    main()
