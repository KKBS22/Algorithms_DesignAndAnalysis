"""
ECE606, F'21, Assignment 2, Problem 4
Skeleton solution file.
"""

import math

"""
You are not allowed to import anything else. You are, however,
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code.
"""


class Node:

    def __init__(self, valData):
        self.data = valData
        self.LNode = None
        self.RNode = None
        pass


class BinarySearchTree():

    def __init__(self, dataList):
        self.initial_list = dataList
        self.bst_list = []
        #value_test = math.floor(math.log2(self.initial_list))
        self.height = math.floor(math.log2(len(self.initial_list)))
        pass

    def create_tree(self):
        root_node_pos = self.find_root()[0]
        root_node = Node(self.find_root()[1])

        left_list_tree = self.initial_list[:root_node_pos]
        right_list_tree = self.initial_list[root_node_pos+1:]

        left_tree_node = self.create_left_right_tree(left_list_tree)
        right_tree_node = self.create_left_right_tree(right_list_tree)

        root_node.LNode = left_tree_node
        root_node.RNode = right_tree_node
        return root_node

    def create_left_right_tree(self, treeData):
        if not treeData:
            return None
        if len(treeData) % 2 == 0:
            mid_val = int(len(treeData) / 2)
        else:
            mid_val = math.floor(len(treeData) / 2)
        root = Node(treeData[mid_val])
        root.LNode = self.create_left_right_tree(treeData[:mid_val])
        root.RNode = self.create_left_right_tree(treeData[mid_val+1:])
        return root

    def find_root(self):
        max_nodes = pow(2, self.height+1)-1
        length_array = len(self.initial_list)
        if (max_nodes == length_array):
            position_root = int((length_array-1)/2)
            return [position_root, self.initial_list[position_root]]
        else:
            node_for_lst_ht = pow(2, self.height)-(max_nodes-length_array)
            nodes_needed = 0
            for a in range(1, self.height+1):
                if a == self.height:
                    nodes_needed = nodes_needed + node_for_lst_ht
                else:
                    nodes_needed = nodes_needed + (pow(2, a)/2)
            nodes_needed = int(nodes_needed)
            #position_root = pow(2, (self.height))-1
            return [nodes_needed, self.initial_list[nodes_needed]]

    def level_order_traversal(self, rootNode):
        bst_list = []
        height_val = self.find_height(rootNode)
        for i in range(1, height_val+1):
            #bst_list.append(self.data_at_level(rootNode, i))
            self.data_at_level(rootNode, i)
        # return bst_list

    def data_at_level(self, node, levelVal):
        bst_list = []
        if node is None:
            return
        if levelVal == 1:
            #print(node.data, end=" ")
            self.bst_list.append(node.data)
        elif levelVal > 1:
            self.data_at_level(node.LNode, levelVal-1)
            self.data_at_level(node.RNode, levelVal-1)
        pass

    def find_height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.find_height(node.LNode)
            right_height = self.find_height(node.RNode)

            # Use the larger one
            if left_height > right_height:
                return left_height+1
            else:
                return right_height+1


def buildbst(s):
    """
    You need to implement this method. See the handout for its specs.
    """
    sorted_set = sorted(s)
    data_as_list = list(sorted_set)
    bstTree = BinarySearchTree(data_as_list)
    root_node_data = bstTree.create_tree()
    #final_encode = bstTree.level_order_traversal(root_node_data)
    bstTree.level_order_traversal(root_node_data)
    return bstTree.bst_list
