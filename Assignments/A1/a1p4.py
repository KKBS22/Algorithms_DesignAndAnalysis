"""
ECE606, F'21, Assignment 1, Problem 4
Skeleton solution file.
"""

"""
You are not allowed to import anything. You are, however,
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code as you like.
"""


def encode(d, i):
    """
    You need to implement this method. See the handout for its specs.
    """
    if (i <= ((pow(10, d)/(2))-1)) and (i >= -(pow(10, d)/(2))):
        return (i % pow(10, d))
    else:
        return (i % pow(10, d))


def decode(d, i):
    """
    You need to implement this method. See the handout for its specs.
    """
    if (i > ((pow(10, d)/2)-1)):
        return (i - pow(10, d))
    else:
        return (i % pow(10, d))


def add(d, i, j):
    """
    You need to implement this method. See  the handout for its specs.
    """
    i_encode = decode(d, i)
    j_encode = decode(d, j)
    return encode(d, (i_encode + j_encode))


def multiply(d, i, j):
    """
    You need to implement this method. See the handout for its specs.
    """
    #i_encode = decode(d, i)
    #j_encode = decode(d, j)
    i_encode = i
    j_encode = j
    if (j_encode == 0):
        return 0
    elif (j_encode == 1):
        return i_encode
    elif (j_encode > 0) and (j_encode % 2 == 0):
        add_result = add(d, i_encode, i_encode)
        return encode(d, multiply(d, add_result, (j_encode//2)))
    else:
        add_result = add(d, i_encode, i_encode)
        return encode(d, i_encode + multiply(d, add_result, (j_encode//2)))
