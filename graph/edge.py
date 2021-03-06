class Edge(object):

    def __init__(self, v, w, weight):

        # 顶点一
        self._v = v
        # 顶点二
        self._w = w
        # 当前边的权重
        self._weight = weight

    def weight(self):
        '''获取边的权重值'''
        return self._weight

    def either(self):
        '''获取边上的一个点'''
        return self._v

    def other(self, t):
        '''获取边上的另外一个点'''
        if t == self._v:
            return self._w
        else:
            return self._v

    def __lt__(self, that):
        '''小于'''
        # 获取边上的一个点
        if self._weight > that._weight:
            # 如果当前边的权重值大，则返回Fasle
            return False
        elif self._weight < that._weight:
            return True
        else:
            return True
