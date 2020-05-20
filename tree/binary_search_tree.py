class Node(object):
    '''树节点'''
    def __init__(self, key: int, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree(object):
    '''排序二叉树（二叉查找树（英语：Binary Search Tree），也称二叉搜索树、有序二叉树）'''

    def __init__(self, root=None):
        # 记录根结点
        self.root = root
        # 记录树中元素的个数
        self.num = 0

    def size(self):
        '''获取树中元素的个数'''
        return self.num

    def insert(self, node: Node, key, value):
        '''向指定的树node中添加key-value,并返回添加元素后新的树'''
        if node is None:
            new_node = Node(key, value, Node, Node)
            if self.root is Node:
                self.root = new_node
            self.num += 1
            return new_node

        if node.key > key:
            node.right = self.insert(node.right, key, value)
        elif node.key < key:
            node.left = self.insert(node.left, key, value)
        else:
            node.value = value
        return node
