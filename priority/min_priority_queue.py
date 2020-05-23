class MinPriorityQueue(object):
    '''
        最小优先队列
        1、最小的元素放在索引为1的位置
        2、每个节点总是小于等于它的子节点的元素
    '''

    def __init__(self, capacity):
        # 堆的元素从索引为1的位置开始储存
        self.item = [None] * (capacity + 1)
        # 记录堆中元素的个数
        self.num = 0

    def less(self, i, j):
        '''判断堆中索引i处的元素是否小于索引j处的元素'''

        return self.item[i] < self.item[j]

    def exch(self, i, j):
        '''交换堆中i索引和j索引处的值'''
        self.item[i], self.item[j] = self.item[j], self.item[i]

    def insert(self, value):
        self.num += 1
        self.item[self.num] = value
        self.swim(self.num)

    def swim(self, k):
        '''使用上浮算法，使索引k处的元素能在堆中处于一个正确的位置'''

        # 通过循环，不断的比较当前结点的值和其父结点的值，如果发现父结点的值比当前结点的值小，则交换位置
        while k > 1:
            # 比较当前结点和其父结点
            if self.less(k, k // 2):
                self.exch(k, k // 2)
            k = k // 2

    def delete_min(self):
        '''删除堆中最小的元素,并返回这个最小元素'''
        if self.num == 0:
            return None

        min_value = self.item[1]
        self.exch(1, self.num)
        # self.item[1], self.item[self.num] = self.item[self.num], self.item[1]

        self.item[self.num] = None

        self.num -= 1
        self.sink(1)
        return min_value

    def sink(self, k):
        '''使用下沉算法，使索引k处的元素能在堆中处于一个正确的位置'''

        # //通过循环不断的对比当前k结点和其左子结点2*k以及右子结点2k+1处中的较大值的元素大小，如果当前结点大，
        # 则需要交换位置
        while 2 * k <= self.num:

            # 获取当前结点的子结点中的较小结点
            if (2 * k + 1) > self.num:
                temp_min = 2 * k
            else:
                if self.less(2*k, 2*k + 1):
                    temp_min = 2*k
                else:
                    temp_min = 2*k + 1

            if self.less(k, temp_min):
                break

            self.exch(k, temp_min)

            k = temp_min

    def size(self):
        return self.num

    def is_empty(self):
        return self.num == 0
