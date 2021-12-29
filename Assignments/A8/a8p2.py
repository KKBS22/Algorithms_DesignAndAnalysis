"""
ECE606, F'21, Assignment 8, Problem 2(b)
Skeleton solution file.
"""

import random

"""
You are not allowed to import anything else. You are
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code.
"""


def avgsatisfied(G, k):
    """
    You need to implement this method. See the handout for its specs.
    NOTE: you should *NOT* modify the argument G. You should assume
          "read-only" access to it only. Make a copy of it first if you
          feel you need to modify it.
    """

    wt_avg = 0
    i = 0
    while i < 5000:
        graph_colored = assign_colors(len(G), k)
        no_satisfied = check_satisfied(graph_colored, G)
        wt_avg += no_satisfied
        i += 1

    return (wt_avg/5000)


def assign_colors(vertices, k):
    graph_coloring = [0]*vertices
    domain_values = [x+1 for x in range(k)]
    for a in range(vertices):
        graph_coloring[a] = random.choices(domain_values)
    return graph_coloring


def check_satisfied(graphColoring, G):
    max_condition = 0
    for a in range(len(G)):
        for b in G[a]:
            if graphColoring[a] != graphColoring[b]:
                max_condition += 1
    return (max_condition/2)
