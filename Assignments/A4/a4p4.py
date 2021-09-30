
graph_set = [[2, 3, 4], [2, 3], [0, 1], [0, 1, 4], [0, 3]]

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
    another_st(graph_set, 2)

    pass


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


"""
Depth First Search CLRS
"""


def get_shortest_path(graphAdjList, source, destination):
    shortest_path = []
    while graphAdjList[destination].parent_node != -1:
        shortest_path.insert(0, destination)
        destination = graphAdjList[destination].parent_node
    shortest_path.insert(0, destination)
    return shortest_path


def DFS():
    pass


if __name__ == '__main__':
    main()
