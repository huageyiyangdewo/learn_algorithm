from graph.depth_first_order import DepthFirstOrder
from graph.directedcycle import DirectedCycle
from copy import deepcopy


class ToPoLogical(object):
    '''拓扑排序'''

    def __init__(self, g):
        self.order = None

        # 因为DirectedCycle检查是否有环时会把队列中的元素出队，导致g中的队列无元素
        t_g = deepcopy(g)
        # 创建一个检测有向环的对象
        di_cycle = DirectedCycle(g)
        if not di_cycle.has_cycle():
            # 判断G图中有没有环，如果没有环，则进行顶点排序：创建一个顶点排序对象
            df_order = DepthFirstOrder(t_g)
            self.order = df_order.get_reverse_post()

    def has_cycle(self):
        '''判断图G是否有环'''
        return self.order is None

    def get_order(self):
        '''获取拓扑排序的所有顶点'''
        return self.order
