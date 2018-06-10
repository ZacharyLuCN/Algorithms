from Textbook.binary_search_tree import BinaryTreeNode, BinaryTree
from Textbook.min_heap import MinHeap


class HuffmanTree(BinaryTree):

    def create_tree(self, data):
        if not (isinstance(data, list) or isinstance(data, tuple)
                or isinstance(data, set)):
            raise TypeError("TypeError：not list/tuple/set")

        if len(data) > 1:
            min_heap = MinHeap()
            min_heap.build_heap(data)
            left_node = BinaryTreeNode(min_heap.pop_top())
            while not min_heap.is_empty():
                right_node = BinaryTreeNode(min_heap.pop_top())
                self.root = BinaryTreeNode(left_node.value + right_node.value)
                self.root.left_child = left_node
                self.root.right_child = right_node
                left_node = self.root
        elif len(data) == 1:
            # TypeError: 'set' object does not support indexing
            # self.root = BinaryTreeNode(data[0])
            for val in data:
                self.root = BinaryTreeNode(val)
        else:
            return
