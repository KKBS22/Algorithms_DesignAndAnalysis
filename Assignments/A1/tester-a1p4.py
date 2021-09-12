#! /usr/bin/python3

import sys
import random
from a1p4 import encode, decode, add, multiply

"""
Some tests.

If you set this file to executable, and have the a1p4.py file in
the same folder, then you should be able to run this.
"""


def main():
    print('Test 1:', end=' ')
    failure = False
    ret = encode(2, -15)

    if ((not ret) or (ret != 85)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 2:', end=' ')
    failure = False
    ret = encode(4, 5000)

    if ((not ret) or (ret != 5000)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 3:', end=' ')
    failure = False
    ret = decode(2, 85)

    if ((not ret) or (ret != -15)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 4:', end=' ')
    failure = False
    ret = add(3, 412, 23)

    if ((not ret) or (ret != 435)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 5:', end=' ')
    failure = False
    ret = add(3, 412, 895)

    if ((not ret) or (ret != 307)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 6:', end=' ')
    failure = False
    ret = multiply(2, 13, 11)

    if ((not ret) or (ret != 43)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 7:', end=' ')
    failure = False
    ret = multiply(3, 412, 895)

    if ((not ret) or (ret != 740)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 8:', end=' ')
    failure = False
    ret = multiply(2, 24, 24)

    if ((not ret) or (ret != 76)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    """
    Test Case : By Piazza post Question 39
    """
    print('Test 9:', end=' ')
    failure = False
    ret = multiply(2, 13, 89)

    if ((not ret) or (ret != 57)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 10:', end=' ')
    failure = False
    ret = multiply(4, 1813, 1113)

    if ((not ret) or (ret != 7869)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 11:', end=' ')
    failure = False
    ret = multiply(2, 89, 13)

    if ((not ret) or (ret != 57)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 12:', end=' ')
    failure = False
    ret = multiply(2, 15, 11)

    if ((not ret) or (ret != 65)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')


if __name__ == '__main__':
    main()
