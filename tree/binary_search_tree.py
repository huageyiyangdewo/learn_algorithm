from linear.singlelinklist import SingleLinkList
from queue_l.queue_link import Queue


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

    def _min(self, node: Node):

        if node is None:
            return Node

        while node.left is not None:
            node = node.left
        return node.key

    # 查找整个树中最小的键
    def min(self):
        return self._min(self.root)

    def _max(self, node: Node):

        if node is None:
            return Node

        while node.right is not None:
            node = node.right
        return node.key

    # 查找整个树中最大的键
    def max(self):
        return self._max(self.root)

    def _pre_ergodic(self, node: Node, que: SingleLinkList):
        if node is None:
            return None

        que.append(node)
        if node.left is not None:
            self._pre_ergodic(node.left, que)
        if node.right is not None:
            self._pre_ergodic(node.right, que)

    # 获取指定树x的所有键，并放到keys队列中
    def pre_ergodic(self):
        '''前序遍历：先遍历根节点，再遍历左子树，再右子树'''
        keys = SingleLinkList()
        self._pre_ergodic(self.root, keys)
        return keys

    def _mid_ergodic(self, node: Node, que: SingleLinkList):
        if node is None:
            return node

        if node.left is not None:
            self._mid_ergodic(node.left, que)

        que.append(node)

        if node.right is not None:
            self._mid_ergodic(node.right, que)

    def mid_ergodic(self):
        '''中序遍历：先遍历左子树，再遍历根节点，再右子树'''
        keys = SingleLinkList()
        self._mid_ergodic(self.root, keys)
        return keys

    def _suf_ergodic(self, node: Node, que: SingleLinkList):
        if node is None:
            return node

        if node.left is not None:
            self._suf_ergodic(node.left, que)

        if node.right is not None:
            self._suf_ergodic(node.right, que)

        que.append(node)

    def suf_ergodic(self):
        '''后序遍历：先遍历左子树，再遍历右子树，再根节点'''
        keys = SingleLinkList()
        self._suf_ergodic(self.root, keys)
        return keys

    def layer_ergodic(self):
        '''层序遍历：从根节点开始，依次往下，获取每一层节点的所有值'''
        # 存储所有的节点
        keys = Queue()
        # 辅助队列
        nodes = Queue()

        nodes.enqueue(self.root)

        while not nodes.is_empty():
            # 从队列中弹出一个结点，把key放入到keys中
            temp = nodes.dequeue()
            keys.enqueue(temp)

            # 判断当前结点还有没有左子结点，如果有，则放入到nodes中
            if temp.left is not None:
                nodes.enqueue(temp.left)
            # 判断当前结点还有没有右子结点，如果有，则放入到nodes中
            if temp.right is not None:
                nodes.enqueue(temp.right)
        return keys

    def _max_depth(self, node: Node):
        if node is None:
            return 0

        # node的最大深度
        max_node = 0
        # 左子树的最大深度
        max_l = 0
        # 右子树的最大深度
        max_r = 0

        # 计算node结点左子树的最大深度
        if node.left is not None:
            max_l = self._max_depth(node.left)

        if node.right is not None:
            max_r = self._max_depth(node.right)

        # 比较左子树最大深度和右子树最大深度，取较大值+1即可
        max_node = max_l + 1 if max_l > max_r else max_r + 1
        return max_node

    def max_depth(self):
        '''获取整个树的最大深度'''
        return self._max_depth(self.root)
