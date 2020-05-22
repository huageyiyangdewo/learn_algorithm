from linear.singlelinklist import SingleNode


class Queue(object):
    """队列 先进先出（FIFO）"""
    def __init__(self):
        self._head = SingleNode(None)
        self._last = None
        self.num = 0

    def __iter__(self):
        '''实现可迭代对象'''
        cur = self._head.next
        while cur.next is not None:
            yield cur
            cur = cur.next
        yield cur

    def is_empty(self):
        return self.num == 0

    def enqueue(self, item):
        """进队列"""
        new_node = SingleNode(item)
        if self.is_empty():
            self._last = new_node
            self._head.next = self._last
        else:
            temp = self._last
            self._last = new_node
            temp.next = self._last
        self.num += 1

    def dequeue(self):
        """出队列"""
        if self.is_empty():
            return False
        else:
            ret = self._head.next.item
            old_first = self._head.next

            self._head.next = old_first.next
            self.num -= 1
            if self.is_empty():
                self._last = None
            return ret

    def size(self):
        """返回大小"""
        return self.num
