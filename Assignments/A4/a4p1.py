"""
ECE606, F'21, Assignment 4, Problem 1
Skeleton solution file.
"""

"""
You are not allowed to import anything. You are, however,
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code.
"""


def anotherst(G, T):
    """
    You need to implement this method. See the handout for its specs.
    """
    edges_out = find_disconnected_edges(G, T)
    count_add = 0
    for a in range(len(T)):
        if len(edges_out[a]) >= 1:
            count_add = count_add + 1
            if count_add == 1:
                T[a].append(edges_out[a][0])
                T[edges_out[a][0]].append(a)
                for node in T[edges_out[a][0]]:
                    if node != a:
                        T[edges_out[a][0]].remove(node)
                        T[node].remove(edges_out[a][0])
            else:
                break
    st_new = T
    return st_new


def find_disconnected_edges(graphAdjList, spanningTree):
    edges_removed = []
    for a in range(len(graphAdjList)):
        rem_list = set(graphAdjList[a]).difference(set(spanningTree[a]))
        edges_removed.append(list(rem_list))
    return edges_removed
