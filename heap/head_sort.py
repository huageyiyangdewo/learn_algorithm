from copy import deepcopy


class HeapSort(object):
    '''堆排序'''

    @staticmethod
    def less(item, i, j):
        '''判断堆中索引i处的元素是否小于索引j处的元素'''

        return item[i] < item[j]

    @staticmethod
    def exch(item, i, j):
        '''交换堆中i索引和j索引处的值'''
        item[i], item[j] = item[j], item[i]

    @staticmethod
    def create_heap(source):
        '''根据原数组source，构造出堆heap'''
        # 把source中的元素拷贝到heap中，heap中的元素就形成一个无序的堆
        heap = deepcopy(source)
        heap.insert(0, None)

        # 对堆中的元素做下沉调整(从长度的一半处开始，往索引1处扫描)
        for i in range(len(source) // 2, 0, -1):
            HeapSort.sink(heap, i, len(source)-1)
        return heap

    @staticmethod
    def sink(heap, k, num):
        '''使用下沉算法，使索引k处的元素能在堆中处于一个正确的位置'''

        # //通过循环不断的对比当前k结点和其左子结点2*k以及右子结点2k+1处中的较大值的元素大小，如果当前结点小，
        # 则需要交换位置
        while 2 * k <= num:

            # 获取当前结点的子结点中的较大结点
            if (2 * k + 1) > num:
                temp_max = 2 * k
            else:
                if HeapSort.less(heap, 2 * k, 2 * k + 1):
                    temp_max = 2 * k + 1
                else:
                    temp_max = 2 * k

            if HeapSort.less(heap, temp_max, k):
                break

            HeapSort.exch(heap, temp_max, k)

            k = temp_max

    @staticmethod
    def sort(source):
        '''堆排序'''
        # 构建堆
        head = HeapSort.create_heap(source)

        # 定义一个变量，记录未排序的元素中最大的索引
        max_n = len(source)

        # 通过循环，交换1索引处的元素和排序的元素中最大的索引处的元素
        while max_n != 1:
            HeapSort.exch(head, 1, max_n)

            max_n -= 1

            HeapSort.sink(head, 1, max_n)

        return head[1:]
