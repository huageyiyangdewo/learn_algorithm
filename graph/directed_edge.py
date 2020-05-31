class DirectedEdge(object):
    '''有向边'''

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

    def from_v(self):
        '''获取有向边的起点'''
        return self._v

    def to(self):
        '''获取有向边的终点'''
        return self._w
