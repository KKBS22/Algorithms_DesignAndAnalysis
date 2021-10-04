
graph_set = [[2, 3, 4], [2, 3], [0, 1], [0, 1, 4], [0, 3]]
spanning_tree = [[2, 3], [3], [0], [0, 1, 4], [3]]
directed_graph_set = [[1, 5], [4], [4, 3], [3], [5], [1]]


"""
Class to define a Node:
1. Color:
    White = 0
    Grey = 1
    Black = 2
"""


class Node:

    def __init__(self, dataValue):
        self.data = dataValue
        self.color = 0
        self.depth = 0
        self.parent_node = -1
        self.node_list = []
        self.start_time = 0
        self.end_time = 0
        pass


def generate_nodes(adjacencyList):
    list_of_nodes = []
    for element in range(len(adjacencyList)):
        aTest = Node(element)
        list_of_nodes.append(aTest)
    for element in range(len(adjacencyList)):
        for a in adjacencyList[element]:
            list_of_nodes[element].node_list.append(list_of_nodes[a])
    return list_of_nodes


def main():
    #another_st(graph_set, 2)
    # edges_out = find_disconnected_edges(graph_set, spanning_tree)
    # count_add = 0
    # for a in range(len(spanning_tree)):
    #     if len(edges_out[a]) >= 1:
    #         count_add = count_add + 1
    #         if count_add == 1:
    #             spanning_tree[a].append(edges_out[a][0])
    #             spanning_tree[edges_out[a][0]].append(a)
    #             for node in spanning_tree[edges_out[a][0]]:
    #                 if node != a:
    #                     spanning_tree[edges_out[a][0]].remove(node)
    #                     spanning_tree[node].remove(edges_out[a][0])
    #         else:
    #             break
    # st_new = spanning_tree
    spanning_tree_prime = anotherst(graph_set, spanning_tree)
    print(spanning_tree_prime)


def anotherst(graphAdjList, initST):
    edges_out = find_disconnected_edges(graphAdjList, initST)
    count_add = 0
    for a in range(len(initST)):
        if len(edges_out[a]) >= 1:
            count_add = count_add + 1
            if count_add == 1:
                initST[a].append(edges_out[a][0])
                initST[edges_out[a][0]].append(a)
                for node in initST[edges_out[a][0]]:
                    if node != a:
                        initST[edges_out[a][0]].remove(node)
                        initST[node].remove(edges_out[a][0])
            else:
                break
    st_new = initST
    return st_new


def another_st(graphAdjList, InitST):
    node_list = generate_nodes(graphAdjList)
    BFS_search = BFS(node_list, 0, 1)
    short_path = get_shortest_path(node_list, 0, 1)
    for a in BFS_search:
        print(a.data)
    print(short_path)


"""
Breadth First Search CLRS
"""


def BFS(graphAdjList, startNode, method):
    visited_list = []
    path_list = []
    if method == 1:
        graphAdjList[startNode].color = 1
        graphAdjList[startNode].depth = 0
        graphAdjList[startNode].parent_node = -1
        visited_list.append(graphAdjList[startNode])
        path_list.append(graphAdjList[startNode])
        while len(visited_list) != 0:
            pop_item = visited_list.pop(0)
            for a in graphAdjList[pop_item.data].node_list:
                if a.color == 0:
                    a.color = 1
                    a.depth = graphAdjList[pop_item.data].depth + 1
                    a.parent_node = graphAdjList[pop_item.data].data
                    visited_list.append(a)
                    path_list.append(a)
            graphAdjList[pop_item.data].color = 2
    return path_list


def get_shortest_path(graphAdjList, source, destination):
    shortest_path = []
    while graphAdjList[destination].parent_node != -1:
        shortest_path.insert(0, destination)
        destination = graphAdjList[destination].parent_node
    shortest_path.insert(0, destination)
    return shortest_path


def find_disconnected_edges(graphAdjList, spanningTree):
    edges_removed = []
    for a in range(len(graphAdjList)):
        rem_list = set(graphAdjList[a]).difference(set(spanningTree[a]))
        edges_removed.append(list(rem_list))
    return edges_removed


# TODO
"""
Depth First Search for directed graph CLRS
"""


# def DFS(graphAdjList):
#     node_list = generate_nodes(graphAdjList)
#     for aNode in
#     pass


# def DFS_visit(node):
#     pass


"""
Depth First Search for undirected graph CLRS
"""


def DFS_undirected():
    pass


if __name__ == '__main__':
    main()
