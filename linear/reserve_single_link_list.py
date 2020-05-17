from linear.singlelinklist import SingleLinkList, SingleNode


class ReserveSingleLinkList(object):

    @staticmethod
    def reserve_by_head_add(s_link):
        '''反转单链表，通过建立新的链表，使用头插的方式'''

        if s_link.is_empty():
            return s_link

        new_link = SingleLinkList()

        cur = s_link._head
        while cur is not None:
            new_link.add(cur.item)
            cur = cur.next

        return new_link

    @staticmethod
    def reserve_by_3_pointer(s_link):
        '''利用三个指针p0"前指针"、p1“当前指针”、p2"后指针"来分批处理链表元素。
        p0置为NULL，它将作为链表的尾结点向前推进处理，
        p1指向旧链表的头指针head，
        p2指向旧链表的头指针的next结点。
        '''
        p0 = None
        p1 = s_link._head

        if p1 is None or p1.next is None:
            return s_link
        p2 = p1.next
        while p1 is not None:

            # temp_pointer = p1
            p1.next = p0
            # p0作为头结点，指向旧链表中的第一个节点
            p0 = p1

            # p1指向p1.next
            p1 = p2
            # p1.next = p2
            # p2不为None，说明p2不是尾节点
            if p2 is not None:
                p2 = p2.next

        return SingleLinkList(p0)
