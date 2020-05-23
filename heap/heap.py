class Heap(object):
    '''
    堆
    1、完全二叉查找树：除了树最后一层节点不需要是满的外，其他的每一层从左往右都是满的，如果最后一层不是满的，
        要求左满右不满
    2、通常使用列表来存储元素：将二叉树的节点按照层级顺序放入列表中，根节点位置为1，它的子节点为在2和3出，而子节点的子节点
        则分别在4和5、6和7的位置，依次类推
        一个节点的位置为k,则父结点的位置为 k/2, 子节点的位置为2k和2k+1
    3、每个节点都大于等于它的两个子节点，注意：两个子节点的顺序是没有关系的
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
            if not self.less(k, k // 2):
                self.exch(k, k // 2)
            k = k // 2

    def delete_max(self):
        '''删除堆中最大的元素,并返回这个最大元素'''
        if self.num == 0:
            return None

        max_value = self.item[1]
        self.item[1], self.item[self.num] = self.item[self.num], self.item[1]

        self.item[self.num] = None

        self.num -= 1
        self.sink(1)
        return max_value

    def sink(self, k):
        '''使用下沉算法，使索引k处的元素能在堆中处于一个正确的位置'''

        # //通过循环不断的对比当前k结点和其左子结点2*k以及右子结点2k+1处中的较大值的元素大小，如果当前结点小，
        # 则需要交换位置
        while 2 * k <= self.num:

            # 获取当前结点的子结点中的较大结点
            if (2 * k + 1) > self.num:
                temp_max = 2 * k
            else:
                if self.less(2*k, 2*k + 1):
                    temp_max = 2*k + 1
                else:
                    temp_max = 2*k

            if self.less(temp_max, k):
                break

            self.exch(temp_max, k)

            k = temp_max
