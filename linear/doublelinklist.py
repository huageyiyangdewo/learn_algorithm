class DoubleNode(object):

    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    '''双链表'''

    def __init__(self):

        self._head = None

    def is_empty(self):
        # 是否为空链表
        return self._head is None

    def length(self):
        # 返回链表长度
        if self.is_empty():
            return 0

        cur = self._head
        count = 0
        while cur.next is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历
        if self.is_empty():
            print('double link list is None')

        cur = self._head
        while cur is not None:
            print(cur.item)
            cur = cur.next

    def add(self, item):
        # 头部插入数据
        node = DoubleNode(item)
        if self.is_empty():
            self._head = node

        else:

            # 新节点的next指向之前的头结点
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self, item):
        """尾部插入元素"""
        node = DoubleNode(item)
        if self.is_empty():
            self.add(item)
        else:

            cur = self._head
            while cur.next is not None:
                cur = cur.next

            cur.next = node
            node.prev = cur

    def search(self, item):
        """查找元素是否存在"""

        if self.is_empty():
            return False
        else:
            cur = self._head
            while cur.next is not None:
                if cur.item == item:
                    return True
                cur = cur.next
            return False

    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        # 位置从0开始算
        elif pos > (self.length()-1):
            self.append(item)
        # 找到指定位置
        else:
            node = DoubleNode(item)
            cur_pos = 0
            cur = self._head
            while cur_pos != pos:
                cur = cur.next
                cur_pos += 1

            node.prev = cur.prev
            node.next = cur
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除元素"""

        if self.is_empty():
            return None
        else:

            cur = self._head
            # if cur.item == item:
            #     # 第一个元素为要删除的元素
            #     if cur.next is None:
            #         # 只有一个元素时
            #         self._head = None
            #     else:
            #         cur.next.prev = None
            #         self._head = cur.next
            # else:
            while cur is not None:
                if cur.item == item:

                    # 删除该元素
                    if cur.prev is None:
                        # 第一个元素
                        # 第一个元素为要删除的元素
                        if cur.next is None:
                            # 只有一个元素时
                            self._head = None
                        else:
                            cur.next.prev = None
                            self._head = cur.next
                    else:
                        cur.prev.next = cur.next

                    if cur.next is None:
                        # 最后一个元素
                        pass
                    else:
                        cur.next.prev = cur.prev
                    break

                cur = cur.next

    def get(self, i):
        # 获取i处的元素
        if i < 0 or self.is_empty():
            return -1

        cur = self._head
        cur_index = 0
        while cur is not None:
            if cur_index == i:
                return cur.item

            cur_index += 1
            cur = cur.next

        return -1

