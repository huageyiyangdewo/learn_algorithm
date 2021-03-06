class SingleNode(object):
    """单链表的结点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self, _head=None):
        self._head = _head

    def __iter__(self):
        '''实现可迭代对象'''
        cur = self._head
        while cur.next is not None:
            yield cur
            cur = cur.next
        yield cur

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur is not None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur is not None:
            print(cur.item)
            cur = cur.next

    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node

    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

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
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur is not None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
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

    def reserve(self):
        '''反转链表'''

        # 判断链表是否为空，为空则返回，否则调用node_reserve方法，反转每一个节点
        if self.is_empty():
            return None

        self.node_reserve(self._head)

    def node_reserve(self, curr):
        '''反转指定的结点curr，并把反转后的结点返回'''

        if curr.next is None:
            self._head = curr
            return curr

        # 递归的反转当前结点curr的下一个结点；返回值就是链表反转后，当前结点的上一个结点
        prev = self.node_reserve(curr.next)

        # 让返回的结点的下一个结点变为当前结点curr；
        prev.next = curr

        # 把当前结点的下一个结点变为null
        curr.next = None
        return curr

    def get_mid(self):
        '''通过快慢指针的方式，获取链表中的中间值
            快指针步长一般为慢指针两倍
        '''

        fast = slow = self._head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow.item




