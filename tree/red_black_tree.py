class Node(object):
    '''节点类'''

    def __init__(self, key, value, left, right, color):
        # 存储键
        self.key = key
        self.value = value
        # 记录左子结点
        self.left = left
        self.right = right
        # 由其父结点指向它的链接的颜色
        self.color = color


class RedBlackTree(object):

    # 红色链接
    RED = True
    # 黑色链接
    BLACK = False

    def __init__(self):
        # 记录树中元素的个数
        self.num = 0
        # 根节点
        self._root = None

    def size(self):
        '''获取树中元素的个数'''
        return self.num

    def is_red(self, node):
        '''判断当前节点的父指向链接是否为红色'''
        return node.color is self.RED

    def rotate_left(self, h):
        '''左旋'''
        # 找到h结点的右子结点x
        x = h.right
        # 找到x结点的左子结点，让x结点的左子结点称为h结点的右子结点
        h.right = x.left
        # 让h结点称为x结点的左子结点
        x.left = h
        # 让x结点的color属性变为h结点的color属性
        x.color = h.color
        # 让h结点的color属性变为RED
        h.color = self.RED
        return x

    def rotate_right(self, h):
        '''右旋'''
        # 找到h结点的左子结点x
        x = h.left
        # 让x结点的右子结点成为h结点的左子结点
        h.left = x.right
        # 让h结点成为x结点的右子结点
        x.right = h
        # 让x结点的color属性变为h结点的color属性
        x.color = h.color
        # 让h结点的color属性变为RED
        h.color = self.RED
        return x

    def flip_color(self, h):
        '''颜色反转,相当于完成拆分4-节点'''
        # 当前结点变为红色
        h.color = self.RED

        # 左子结点和右子结点变为黑色
        h.left.color = self.BLACK
        h.right.color = self.RED

    def put(self, key, value):
        '''在整个树上完成插入操作'''
        self._root = self._put(self._root, key, value)
        # 根结点的颜色总是黑色
        self._root.color = self.BLACK

    def _put(self, h, key, value):
        '''在指定树中，完成插入操作,并返回添加元素后新的树'''

        # 判断h是否为空，如果为空则直接返回一个红色的结点就可以了
        if h is None:
            self.num += 1
            new_node = Node(key, value, None, None, self.RED)
            return new_node

        # 比较h结点的键和key的大小
        if h.key > key:
            h.left = self._put(h.left, key, value)
        elif h.key < key:
            h.right = self._put(h.right, key, value)
        else:
            h.value = value

        # 进行左旋:当当前结点h的左子结点为黑色，右子结点为红色，需要左旋
        if h.left and h.right and not self.is_red(h.left) and self.is_red(h.right):
            h = self.rotate_left(h)

        # 进行右旋：当当前结点h的左子结点和左子结点的左子结点都为红色，需要右旋
        if h.left and h.left.left and self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)

        # 颜色反转：当前结点的左子结点和右子结点都为红色时，需要颜色反转
        if h.left and h.right and self.is_red(h.left) and self.is_red(h.right):
            self.flip_color(h)

        return h

    def get(self, key):
        '''根据key，从树中找出对应的值'''
        return self._get(self._root, key)

    def _get(self, node, key):
        '''从指定的树x中，查找key对应的值'''

        if node is None:
            return None

        if node.key > key:
            return self._get(node.left, key)
        elif node.key < key:
            return self._get(node.right, key)
        else:
            return node.value
