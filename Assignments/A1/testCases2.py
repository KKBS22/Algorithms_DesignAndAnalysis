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
    overall = 0
    passed = 0
    failed = 0
    for test in range(1, 3):  # Range of d
        new = pow(10, test)
        print("new :", new)
        for i in range(0, new):
            for j in range(0, new):
                print("i: ", i, "j :", j)
                overall += 1
                add_result = (i + j) % pow(10, test)
                calculated_result = add(test, i, j)
                if add_result == calculated_result:
                    print("Add - d: ", test, "i: ", i, "j: ", j, "-Passed")
                    passed += 1
                else:
                    print("Add - d: ", test, "i: ", i, "j: ", j, "-Failed")
                    failed += 1

                overall += 1
                multiply_result = (i * j) % pow(10, test)
                cal_result = multiply(test, i, j)

                if multiply_result == cal_result:
                    passed += 1
                    print("Multiply - d: ", test,
                          "i: ", i, "j: ", j, "-Passed")
                else:
                    failed += 1
                    print("Multiply - d: ", test,
                          "i: ", i, "j: ", j, "-Failed")

    print("\n\nOverall Test Cases: ", overall,
          "Passed :", passed, "Failed :", failed)


if __name__ == '__main__':
    main()
