class CycleLinkCheck(object):

    @staticmethod
    def is_cycle(s_link):
        '''
        通过快慢指针判断单链表是否有环
        :param s_link:
        :return:  True/ False
        '''

        if s_link is None:
            return False
        fast = slow = s_link._head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            # 快指针的地址和慢指针的地址相同，则说明有环
            if fast is slow:
                return True
        return False

    @staticmethod
    def get_entrance(s_link):
        '''
        通过快慢指针找到有环链表的入口
        :param s_link:
        :return: 入口节点
        '''
        if s_link is None:
            return False
        fast = slow = s_link._head
        temp = None  # 临时指针

        # 遍历链表，先找到环(快慢指针相遇),准备一个临时指针，
        # 指向链表的首结点，继续遍历，直到慢指针和临时指针相遇，那么相遇时所指向的结点就是环的入口
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            # 快指针的地址和慢指针的地址相同，则说明有环
            if fast is slow:
                temp = s_link._head
                # 注意，这里必须加continue
                continue

            if temp is not None:
                temp = temp.next
                # 临时指针和慢指针相遇，找到入口
                if temp is slow:
                    break

        return temp

