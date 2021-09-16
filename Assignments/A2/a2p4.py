import math


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
        position_root = pow(2, (self.height))-1
        return [position_root, self.initial_list[position_root]]

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


# def printLevelOrder(root):
#     h = height(root)
#     for i in range(1, h+1):
#         printCurrentLevel(root, i)


# # Print nodes at a current level
# def printCurrentLevel(root, level):
#     if root is None:
#         return
#     if level == 1:
#         print(root.data, end=" ")
#     elif level > 1:
#         printCurrentLevel(root.left, level-1)
#         printCurrentLevel(root.right, level-1)


# def height(node):
#     if node is None:
#         return 0
#     else:
#         # Compute the height of each subtree
#         lheight = height(node.left)
#         rheight = height(node.right)

#         # Use the larger one
#         if lheight > rheight:
#             return lheight+1
#         else:
#             return rheight+1


def main():
    data_List = [1, 2, 3, 4, 5, 6]
    bstTree = BinarySearchTree(data_List)
    root_node_data = bstTree.create_tree()
    #final_encode = bstTree.level_order_traversal(root_node_data)
    bstTree.level_order_traversal(root_node_data)
    print(bstTree.bst_list)

    c = 1+1
    pass


if __name__ == '__main__':
    main()
