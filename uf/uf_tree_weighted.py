class UFTreeWeighted(object):
    '''并查集 优化'''

    def __init__(self, n):
        # 记录并查集中数据的分组个数
        # 初始化分组的数量,默认情况下，有N个分组
        self.n = n
        # 记录结点元素和该元素所在分组的标识
        # 初始化eleAndGroup中的元素及其所在的组的标识符,让eleAndGroup数组的索引作为并查集的每个结点的元素，
        # 并且让每个索引处的值(该元素所在的组的标识符)就是该索引
        self.ele_and_group = [i for i in range(n)]

        # 用来存储每一个根结点对应的树中保存的结点的个数,初始为1
        self.sz = [1] * n

    def count(self):
        '''获取当前并查集中的数据有多少个分组'''

        return self.n

    def find(self, p):
        '''元素p所在分组的标识符'''
        while True:
            if p == self.ele_and_group[p]:
                return p
            p = self.ele_and_group[p]

    def connected(self, p, q):
        '''判断并查集中元素p和元素q是否在同一分组中'''

        return self.find(p) == self.find(q)

    def union(self, p, q):
        '''把p元素所在分组和q元素所在分组合并'''

        # 找到p所在分组的标识符
        p_root = self.find(p)
        q_root = self.find(q)

        # 判断元素q和p是否已经在同一分组中，如果已经在同一分组中，则结束方法就可以了
        if p_root == q_root:
            return None

        # 合并组：判断proot对应的树大还是qroot对应的树大，最终需要把较小的树合并到较大的树中
        if self.sz[p_root] > self.sz[q_root]:
            self.ele_and_group[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]
        else:
            self.ele_and_group[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]

        self.n -= 1
