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

