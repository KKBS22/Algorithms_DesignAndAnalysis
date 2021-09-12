#! /usr/bin/python3

import sys
import random
from a1p4 import encode, decode, add, multiply

"""
Some tests.

If you set this file to executable, and have the a1p4.py file in
the same folder, then you should be able to run this.

Test Format:
["Operation", "Digits", "Expected output", **Inputs ]
"""
test_data = [
    [1, 2, 58, -42],
    [1, 3, 455, 455],
    [1, 4, 6411, -3589],
    [1, 5, 54039, -45961],
    [1, 2, 33, 33],
    [1, 6, 5411, 5411],
    [2, 2, -42, 58],
    [2, 3, 455, 455],
    [2, 4, -3589, 6411],
    [2, 5, -45961, 54039],
    [2, 2, 33, 33],
    [2, 6, 5411, 5411],
    [3, 2, 63, 58, 5],
    [3, 3, 800, 455, 345],
    [3, 4, 6514, 6411, 103],
    [3, 5, 95383, 54039, 41344],
    [3, 2, 78, 33, 45],
    [3, 6, 9911, 5411, 4500],
    [4, 2, 90, 58, 5],
    [4, 3, 975, 455, 345],
    [4, 4, 333, 6411, 103],
    [4, 5, 88416, 54039, 41344],
    [4, 2, 85, 33, 45],
    [4, 6, 349500, 5411, 4500],
    [4, 10, 7246144512, 4544, 98425648]
]


def main():
    overall = 0
    for test in test_data:
        if test[0] == 1:
            print("Testing encode()")
            print("Expected Value:", test[2])
            temp = encode(test[1], test[3])
            print("Actual Value:  ", temp, end=" ")
            if test[2] == temp:
                print("Passed")
            else:
                print("!! Failed !!")
                overall += 1
        if test[0] == 2:
            print("Testing decode()")
            print("Expected Value:", test[2])
            temp = decode(test[1], test[3])
            print("Actual Value:  ", temp, end=" ")
            if test[2] == temp:
                print("Passed")
            else:
                print("!! Failed !!")
                overall += 1
        if test[0] == 3:
            print("Testing add()")
            print("Expected Value:", test[2])
            temp = add(test[1], test[3], test[4])
            print("Actual Value:  ", temp, end=" ")
            if test[2] == temp:
                print("Passed")
            else:
                print("!! Failed !!")
                overall += 1
        if test[0] == 4:
            print("Testing multiply()")
            print("Expected Value:", test[2])
            temp = multiply(test[1], test[3], test[4])
            print("Actual Value:  ", temp, end=" ")
            if test[2] == temp:
                print("Passed")
            else:
                print("!! Failed !!")
                overall += 1
    print("\n\nOveall Failed Test Cases: ", overall)


if __name__ == '__main__':
    main()
