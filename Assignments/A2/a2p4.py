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

    def create_tree(self, method):
        if (method == 1):
            root_node_pos = self.find_root(2, self.initial_list)[0]
            root_node = Node(self.find_root(2, self.initial_list)[1])

            left_list_tree = self.initial_list[:root_node_pos]
            right_list_tree = self.initial_list[root_node_pos+1:]

            left_tree_node = self.create_left_right_tree(left_list_tree)
            right_tree_node = self.create_left_right_tree(right_list_tree)

            root_node.LNode = left_tree_node
            root_node.RNode = right_tree_node
        elif(method == 2):
            root_node = self.inorder_array(2, self.initial_list)
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

    def find_root(self, method, subArray):
        int_height = math.floor(math.log2(len(subArray)))
        max_nodes = pow(2, int_height+1)-1
        length_array = len(subArray)

        if (method == 1):
            if (max_nodes == length_array):
                position_root = int((length_array-1)/2)
                return [position_root, subArray[position_root]]
            else:
                node_for_lst_ht = pow(2, int_height)-(max_nodes-length_array)
                nodes_needed = 0
                for a in range(1, int_height+1):
                    if a == int_height:
                        nodes_needed = nodes_needed + node_for_lst_ht
                    else:
                        nodes_needed = nodes_needed + (pow(2, a)/2)
                nodes_needed = int(nodes_needed)
                #position_root = pow(2, (self.height))-1
            return [nodes_needed, self.initial_list[nodes_needed]]
        elif (method == 2):
            if (max_nodes == length_array):
                position_root = int((length_array-1)/2)
                return [position_root, subArray[position_root]]
            else:
                less_by = max_nodes - length_array
                nodes_in_ht = pow(2, int_height)
                lst_needed = nodes_in_ht - less_by
                left_needed = int(pow(2, int_height)/2)
                if (lst_needed >= left_needed):
                    nodes_needed_last = left_needed
                else:
                    nodes_needed_last = left_needed - lst_needed
                nodes_needed = 0
                for a in range(1, int_height+1):
                    if a == int_height:
                        nodes_needed = nodes_needed + nodes_needed_last
                    else:
                        nodes_needed = nodes_needed + (pow(2, a)/2)
                nodes_needed = int(nodes_needed)
            return [nodes_needed, subArray[nodes_needed]]

    def level_order_traversal(self, rootNode):
        bst_list = []
        height_val = self.find_height(rootNode)
        for i in range(1, height_val+1):
            #bst_list.append(self.data_at_level(rootNode, i))
            self.data_at_level(rootNode, i)
        # return bst_list

    def inorder_traversal(self, rootNode):
        if(rootNode is None):
            return
        self.Inorder(rootNode.LNode)
        print(rootNode.value, end=' ')
        self.Inorder(rootNode.RNode)

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

    def inorder_array(self, method, listEle):
        if not listEle:
            return None
        if (method == 1):
            mid = int((len(listEle)) / 2)
            root = Node(listEle[mid])
            root.LNode = self.inorder_array(1, listEle[:mid])
            root.RNode = self.inorder_array(1, listEle[mid+1:])
        elif (method == 2):
            position = self.find_root(2, listEle)[0]
            root = Node(listEle[position])
            root.LNode = self.inorder_array(2, listEle[:position])
            root.RNode = self.inorder_array(
                2, listEle[position+1:])
        return root
        pass


# def search_arr(arr, x, n):

#     for i in range(n):
#         if (arr[i] == x):
#             return i
#     return -1


# def printPostOrder(In, pre, n):
#     post_order = []
#     # The first element in pre[] is always
#     # root, search it in in[] to find left
#     # and right subtrees
#     root = search_arr(In, pre[0], n)

#     # If left subtree is not empty,
#     # print left subtree
#     if (root != 0):
#         printPostOrder(In, pre[1:n], root)

#     # If right subtree is not empty,
#     # print right subtree
#     if (root != n - 1):
#         printPostOrder(In[root + 1: n],
#                        pre[root + 1: n],
#                        n - root - 1)

#     # Print root
#     #print(pre[0], end=" ")
#     post_order.append(pre[0])


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
    data_List = [10, 20, 30, 40, 50, 60, 70,
                 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
    bstTree = BinarySearchTree(data_List)
    bstTree_two = BinarySearchTree(data_List)
    #root_node_data = bstTree.create_tree(1)
    root_node_data_2 = bstTree_two.create_tree(2)
    #final_encode = bstTree.level_order_traversal(root_node_data)
    # bstTree.level_order_traversal(root_node_data)
    bstTree_two.level_order_traversal(root_node_data_2)
    print(bstTree_two.bst_list)

    c = 1+1
    pass


if __name__ == '__main__':
    main()
