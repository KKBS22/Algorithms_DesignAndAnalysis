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
    # T(n) = T(4V+E+17)
    edges_out = find_disconnected_edges(G, T)  # V+E
    if edges_out != None:  # 1
        count_add = 0  # 1
        for a in range(len(T)-1, 0, -1):  # V
            if len(edges_out[a]) >= 1:  # V+1
                count_add = count_add + 1  # V+1 #
                if count_add == 1:  # 2
                    edgeAdd = edges_out[a][0]
                    T[a].append(edges_out[a][0])  # 1
                    T[edges_out[a][0]].append(a)  # 1
                    for node in T[a]:  # 1 + n
                        if node != edgeAdd:  # 1 + n(where n is number of )
                            T[a].remove(node)  # 1
                            T[node].remove(a)  # 1
                else:  # 1
                    break  # 1
        return T  # 1
    else:  # 1
        return None  # 1


def find_disconnected_edges(graphAdjList, spanningTree):
    edges_removed = []
    count_exit = 0
    for a in range(len(graphAdjList)):
        rem_list = set(graphAdjList[a]).difference(set(spanningTree[a]))
        if len(rem_list) == 0:
            count_exit = count_exit + 1
        edges_removed.append(list(rem_list))
    if count_exit == len(graphAdjList):
        return None
    else:
        return edges_removed
