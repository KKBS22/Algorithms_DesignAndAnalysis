"""
ECE606, F'21, Assignment 6, Problem 4
Skeleton solution file.
"""

"""
You are not allowed to import anything. You are
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code.
"""


"""
Method inspired by Prim's Algotihm
"""


def hasmst(G, e):  # O(V^3)
    """
    You need to implement this method. See the handout for its specs.
    NOTE: you should *NOT* modify either of the arguments G, e. You
          have "read-only" access to them only. If you modify them,
          you'll get an automatic 0 on this problem.
    """
    visited_node = [False]*len(G)  # Make all nodes a not visited FALSE # 1
    mst = []  # List to store the minimum spanning tree # 1
    st_nodes = 0  # 1
    visited_node[0] = True  # Set the first node source node as visted TRUE # 1
    while st_nodes <= len(G):  # V
        wt_max = 1000000000000000000000000  # Set max value for the weight # V
        for j in range(len(G)):  # Iterate over all the nodes # V+1
            if visited_node[j]:  # Check if the node is visited # V^2
                # Iteratte through all te nodes form the selected node # VxV^2+1
                for i in range(len(G)):
                    if (not visited_node[i]):  # Check the condition
                        for a in G[j]:  # Iterate through the adjacency list # E
                            if i == a[0]:
                                if wt_max >= a[1]:  # Update minium weght
                                    wt_max = a[1]
                                    src = j
                                    dst = i
        if [src, dst] not in mst:
            mst.append([src, dst])  # Append to MST
        visited_node[dst] = True
        st_nodes = st_nodes+1
    # print(mst)
    test = [0, 0]
    test[0] = e[1]
    test[1] = e[0]
    if ((test in mst) or (e in mst)):  # Compare if present in MST
        return True
    else:
        return False


def hasmstTest(G, e):
    """
    You need to implement this method. See the handout for its specs.
    NOTE: you should *NOT* modify either of the arguments G, e. You
          have "read-only" access to them only. If you modify them,
          you'll get an automatic 0 on this problem.
    """
    mst = [[]]*len(G)
    visited_edge = []
    #print(weight_of_edge(G, e))

    no_edges = len(G)
    # print(no_edges)
    st_edges = no_edges-1
    weight_init = 1000000000000000000000000
    min_edge = [0, 0]
    i = 0
    for a in G:
        i = i+1
        for b in a:
            if weight_init > b[1]:
                weight_init = b[1]
                min_edge[0] = i-1
                min_edge[1] = b[0]
    # print(weight_init)
    #print("min Edge", min_edge)
    mst[min_edge[0]] = [min_edge[1]]
    mst[min_edge[1]] = [min_edge[0]]
    visited_edge.append(min_edge[0])
    visited_edge.append(min_edge[1])
    take_node = min_edge[1]
    # print(mst)
    while len(visited_edge) <= st_edges:
        wt_max = 1000000000000000000000000
        k = 0
        imm_edge = [0, 0]
        for tn in G[take_node]:
            k = k+1
            if tn[0] not in visited_edge:
                if wt_max > tn[1]:
                    wt_max = tn[1]
                    imm_edge[0] = tn[0]
                    imm_edge[1] = tn[1]
                    if imm_edge[0] not in visited_edge:
                        if len(mst[take_node]) != 0:
                            mst[take_node].append(imm_edge[0])
                            if len(mst[imm_edge[0]]) != 0:
                                mst[imm_edge[0]] = [take_node]
                            else:
                                mst[imm_edge[0]].append(take_node)
                        take_node = imm_edge[0]
                        visited_edge.append(take_node)
    # print(mst)
    edge_list = []
    for b in mst[e[0]]:
        edge_list.append([e[0], b])
    # print(edge_list)
    if e in edge_list:
        return True
    else:
        return False

    # for d in range(len(G)):

# def weight_of_edge(G, e):
#     for a in G[e[0]]:
#         if a[0] == e[1]:
#             return a[1]


# def main():
#     print(hasmst([[[2, 10], [1, 10], [3, 30]], [[0, 10], [3, 20]], [
#         [3, 20], [0, 10]], [[1, 20], [2, 20], [0, 30]]], [0, 3]))


# if __name__ == "__main__":
#     main()
