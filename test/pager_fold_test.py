from queue_l.queue_link import Queue


class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class PagerFoldTest(object):

    def __init__(self):
        self.root = None

    def create_tree(self, n):
        '''通过模拟对折N次纸，产生树'''

        for i in range(n):

            # 1.当前是第一次对折
            if i == 0:
                self.root = Node('down', None, None)
                continue

            # 2.当前不是第一次对折
            # 定义辅助队列存储当前对折次数产生的节点,通过层序遍历的思想，找到叶子结点，叶子结点添加子节点
            q = Queue()
            q.enqueue(self.root)
            while not q.is_empty():

                # 从队列中弹出一个结点
                temp = q.dequeue()

                if temp.left is not None:
                    q.enqueue(temp.left)

                if temp.right is not None:
                    q.enqueue(temp.right)

                if temp.left is None and temp.right is None:
                    temp.left = Node('down', None, None)
                    temp.right = Node('up', None, None)

    def _print_tree(self, node):
        '''打印树中每个结点到控制台'''
        # 需要使用中序遍历完成
        if node is None:
            return None

        if node.left is not None:
            self._print_tree(node.left)

        print(node.value, end='  ')
        if node.right is not None:
            self._print_tree(node.right)

    def print_tree(self):
        self._print_tree(self.root)


p = PagerFoldTest()
p.create_tree(2)
p.print_tree()