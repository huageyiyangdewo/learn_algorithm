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

    def _insert(self, key, value, node: Node):
        '''向指定的树node中添加key-value,并返回添加元素后新的树'''
        if node is None:
            self.num += 1
            new_node = Node(key, value, None, None)
            return new_node
        if node.key < key:
            node.right = self._insert(key, value, node.right)
        elif node.key > key:
            node.left = self._insert(key, value, node.left)
        else:
            node.value = value
        return node

    def insert(self, key, value):
        '''插入'''

        if self.root is None:
            new_node = Node(key, value, None, None)
            self.root = new_node
            self.num += 1
            return new_node
        else:
            return self._insert(key, value, self.root)

    def _get(self, key, node: Node):
        if node is None:
            return None

        if node.key < key:
            return self._get(key, node.right)
        elif node.key > key:
            return self._get(key, node.left)
        else:
            return node.value

    def get(self, key):
        '''查找key对应的值'''
        if self.root is None:
            return None

        return self._get(key, self.root)

    def _delete(self, key, node: Node):
        if node is None:
            return None

        if node.key < key:
            # 如果key大于node结点的键，则继续找node结点的右子树
            node.right = self._delete(key, node.right)
        elif node.key > key:
            # 如果key小于node结点的键，则继续找node结点的左子树
            node.left = self._delete(key, node.left)
        else:
            # 如果key等于node结点的键，完成真正的删除结点动作，要删除的结点就是node
            self.num -= 1
            # 找到右子树中最小的节点
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right

            # 右子树中的最小节点
            min_node = node.right
            while min_node.left is not None:
                min_node = min_node.left

            # 删除右子树中最小的结点
            # 最小节点为叶子结点，则让父结点的left=None
            # 最小节点不为叶子节点，则让父结点的left或者right指向min节点的right
            if min_node.left is None and min_node.right is None:
                # 叶子节点
                parent = node.right
                while parent.left is not None:
                    if parent.left.left is None:
                        # 这里就找到了min_mode的父结点
                        parent.left = None
                        break
                    parent = parent.left

            else:
                # 非叶子节点
                if key == self.root.key:
                    parent = self.root
                    while parent.right is not min_node:
                        parent = parent.left
                        if parent.left is None:
                            # 这里就找到了min_mode的父结点
                            parent.left = None
                else:
                    parent = node.right
                    while parent.left is not None:
                        parent = parent.left
                        if parent.left is None:
                            # 这里就找到了min_mode的父结点
                            parent.left = None

                if parent.left is min_node:
                    parent.left = min_node.right
                else:
                    parent.right = min_node.right

            # 让node结点的左子树成为minNode的左子树
            min_node.left = node.left
            # 让node结点的右子树成为minNode的右子树
            min_node.right = node.right
            # 让node结点的父结点指向minNode
            node = min_node
            if key == self.root.key:
                self.root = node

            # 这里为什么返回当前节点就是让node结点的父结点指向minNode，因为递归调用时，用了父结点的子树去接受返回值
            return node

    def delete(self, key):
        '''删除树中key对应的value'''
        if self.root is None:
            return None

        return self._delete(key, self.root)


