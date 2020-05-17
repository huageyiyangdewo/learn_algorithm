from linear.singlelinklist import SingleNode


class StackLink(object):
    """栈 通过链表实现"""

    def __init__(self):
        self._head = None
        self.num = 0

    def is_empty(self):
        """判断是否为空"""
        return self._head is None

    def push(self, item):
        """加入元素"""
        new_node = SingleNode(item)
        old_node = self._head

        self._head = new_node
        self._head.next = old_node
        self.num += 1

    def pop(self):
        """弹出元素"""
        old_node = self._head
        if old_node is None:
            return None
        self._head = old_node.next
        # self._head.next = old_node.next
        self.num -= 1
        return old_node.item

    def peek(self):
        """返回栈顶元素"""
        return self._head

    def size(self):
        """返回栈的大小"""
        return self.num
