class IndexMinPriorityQueue(object):
    '''
        索引最小优先队列
    '''

    def __init__(self, capacity):
        # 存储堆中的元素
        self.item = [None] * (capacity + 1)
        # 保存每个元素在items数组中的索引，pq数组需要堆有序
        self.pq = [None] * (capacity + 1)
        # 保存qp的逆序，pq的值作为索引，pq的索引作为值
        self.qp = [-1] * (capacity + 1)
        # 记录堆中元素的个数
        self.num = 0

    def less(self, i, j):
        '''判断堆中索引i处的元素是否小于索引j处的元素'''

        return self.item[self.pq[i]] < self.item[self.pq[j]]

    def exch(self, i, j):
        '''交换堆中i索引和j索引处的值'''
        # 交换pq中的数据
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

        # 更新qp中的数据
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def contains(self, i):
        # 判断j对应的元素是否存在
        return self.qp[i] != -1

    def min_index(self):
        # 最小元素关联的索引
        return self.pq[1]

    def insert(self, i, value):
        '''往队列中插入一个元素,并关联索引i'''
        # 判断i是否已经被关联，如果已经被关联，则不让插入
        if self.contains(i):
            raise Exception('index exist')

        self.num += 1
        # 把数据存储到items对应的i位置处
        self.item[i] = value

        # 把i存储到pq中
        self.pq[self.num] = i

        # 通过qp来记录pq中的i
        self.qp[i] = self.num

        # 通过堆上浮完成堆的调整
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
        '''删除队列中最小的元素,并返回该元素关联的索引'''
        if self.num == 0:
            return None

        # 获取最小元素关联的索引
        min_index = self.pq[1]

        # 交换pq中索引1处和最大索引处的元素
        self.exch(1, self.num)

        # 删除qp中对应的内容
        self.qp[self.pq[self.num]] = -1

        # 删除pq最大索引处的内容
        self.pq[self.num] = None

        # 删除items中对应的内容
        self.item[min_index] = None

        self.num -= 1
        self.sink(1)
        return min_index

    def delete(self, i):
        '''删除索引i关联的元素'''
        if i < 0 or i > self.num:
            raise Exception('index error')

        # 找到i在pq中的索引
        k = self.qp[i]

        # 交换pq中索引k处的值和索引N处的值
        self.exch(k, self.num)

        # 删除qp中的内容
        self.qp[self.pq[self.num]] = -1

        # 删除pq中的内容,因为和k交换了位置
        self.pq[self.num] = None

        # 删除items中的内容
        self.item[i] = None

        # 元素的数量 - 1
        self.num -= 1
        # 堆的调整
        self.swim(k)
        self.sink(k)

    def change_item(self, i, item):
        '''把与索引i关联的元素修改为为t'''
        if i < 0 or i > self.num:
            raise Exception('index error')

        # 修改items数组中i位置的元素为t
        self.item[i] = item

        # 找到i在pq中出现的位置
        k = self.qp[i]

        self.swim(k)
        self.sink(k)

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
