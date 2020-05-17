from linear.singlelinklist import SingleNode


class Joseph(object):

    @staticmethod
    def create_cycle_link(number):
        '''创建循环链表'''
        first = None
        pre = None
        for i in range(1, number+1):
            if i == 1:
                first = SingleNode(i)
                pre = first
            else:
                temp = SingleNode(i)
                pre.next = temp
                pre = temp
        pre.next = first
        return first

    @staticmethod
    def handle_cycle(first_node):
        temp = first_node
        pre = None  # 记录当前节点的上一个节点
        count = 0
        while temp is not temp.next:
            count += 1
            if count == 3:
                pre.next = temp.next
                print(temp.item, end=',')
                temp = temp.next
                count = 0
            else:
                pre = temp
                temp = temp.next
        print(temp.item)

    @staticmethod
    def main(number=41):
        '''解决约瑟夫问题
            循环链表中，从1报数，报数为3的删除，求最后一个数
        '''
        first_node = Joseph.create_cycle_link(number)
        Joseph.handle_cycle(first_node)


Joseph.main()