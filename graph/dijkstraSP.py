from queue_l.queue_link import Queue
from priority.index_min_priority_queue import IndexMinPriorityQueue
from graph.edge_weight_digraph import EdgeWeightedDiGraph
import math


class DijkstraSP(object):
    '''
    DijkstraSP算法 实现最短路径树
    '''

    def __init__(self, g, s):
        '''根据一副加权有向图G和顶点s，创建一个计算顶点为s的最短路径树对象'''

        # 索引代表顶点，值表示从顶点s到当前顶点的最短路径上的最后一条边
        self.edge_to = [None] * g.v()
        # 索引代表顶点，值从顶点s到当前顶点的最短路径的总权重重 默认无穷大
        self.dist_to = [float('inf')] * g.v()
        # 存放树中顶点与非树中顶点之间的有效横切边
        self.pq = IndexMinPriorityQueue(g.v())

        # 找到图G中以顶点s为起点的最短路径树
        # 默认让顶点s进入到最短路径树中
        self.dist_to[s] = 0.0
        self.pq.insert(s, 0.0)

        # 遍历索引最小优先队列，拿到最小和N切边对应的顶点，把该顶点加入到最短路径树中
        while not self.pq.is_empty():
            self.relax(g, self.pq.delete_min())

    def relax(self, g: EdgeWeightedDiGraph, v: int):
        '''松弛图G中的顶点v'''

        # 更新数据
        while True:
            e = g.adj(v).dequeue()
            if e is False or e is None:
                break
            # 获取到该边的终点w
            w = e.to()

            # 通过松弛技术，判断从起点s到顶点w的最短路径是否需要先从顶点s到顶点v，然后再由顶点v到顶点w
            if self.dist_to[v] + e.weight() < self.dist_to[w]:
                self.dist_to[w] = self.dist_to[v] + e.weight()
                self.edge_to[w] = e
                # 判断pq中是否已经存在顶点w，如果存在，则更新权重，如果不存在，则直接添加
                e_weight = e.weight()
                if self.pq.contains(w):
                    self.pq.change_item(w, e_weight)
                else:
                    self.pq.insert(w, e_weight)

    def get_dist_to(self, v):
        '''获取从顶点s到顶点v的最短路径的总权重'''
        return self.dist_to[v]

    def has_path_to(self, v):
        '''判断从顶点s到顶点v是否可达'''
        return not math.isinf(self.dist_to[v])

    def path_to(self, v):
        '''查询从起点s到顶点v的最短路径中所有的边'''
        # 判断从顶点s到顶点v是否可达，如果不可达，直接返回null
        if not self.has_path_to(v):
            return None

        # 创建队列对象
        all_edges = Queue()
        while True:
            e = self.edge_to[v]
            if e is None:
                break
            all_edges.enqueue(e)
            v = e.from_v()

        return all_edges
