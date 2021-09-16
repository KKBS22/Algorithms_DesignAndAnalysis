#! /usr/bin/python3

import sys
import random
from a2p4_new import buildbst

"""
Some tests.

If you set this file to executable, and have the a1p4.py file in
the same folder, then you should be able to run this.
"""


def checkBst(s, t):
    if(not s or not t or s != set(t) or len(s) != len(t)):
        return False
    for i in range(len(t)//2):
        if (2*i+1 < len(t) and t[2*i+1] >= t[i]):
            return False
        if (2*i+2 < len(t) and t[2*i+2] <= t[i]):
            return False
    return True


def main():
    print('Test 1:', end=' ')
    s = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150}
    t = buildbst(s)
    success = checkBst(s, t)
    if success:
        print('Passed')
    else:
        print('Failed')

    print('Test 2:', end=' ')
    s = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150}
    t = buildbst(s)
    success = checkBst(s, t)
    if success:
        print('Passed')
    else:
        print('Failed')

    print('Test 3:', end=' ')
    s = set()
    s.clear()
    r = random.randint(1000, 2000)
    for i in range(r):
        s.add(random.randint(1, 1000000))
    t = buildbst(s)
    success = checkBst(s, t)
    if success:
        print('Passed')
    else:
        print('Failed')


if __name__ == '__main__':
    main()
