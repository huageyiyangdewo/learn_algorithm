class SymbolNode(object):
    # 符号表的节点类

    def __init__(self, key, value, next_nd):
        self.key = key
        self.value = value
        self.next = next_nd


class OrderSymbolTable(object):
    '''有序符号表'''

    def __init__(self):
        self._head = SymbolNode(None, None, None)
        self.num = 0

    def put(self, key: int, value):
        '''插入键值对'''
        curr = self._head.next
        pre = self._head
        while curr is not None and curr.key != key:
            pre = curr
            curr = curr.next

        if curr is not None and curr.key == key:
            curr.value = value
            return

        # key不存在
        new_node = SymbolNode(key, value, curr)
        pre.next = new_node
        self.num += 1

    def delete(self, key: int):
        '''删除key'''

        head = self._head
        while head.next is not None:
            if head.next.key == key:
                head.next = head.next.next
                self.num -= 1
                return

            head = head.next

    def get(self, key: int):
        head = self._head
        while head.next is not None:
            if head.next.key == key:
                return head.next.value

            head = head.next
        return False

