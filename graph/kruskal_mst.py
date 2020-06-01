from queue_l.queue_link import Queue
from priority.min_priority_queue import MinPriorityQueue
from graph.edge_weight_graph import EdgeWeightedGraph
from uf.uf_tree_weighted import UFTreeWeighted


class KruskalMST(object):
    '''
    kruskal算法
    主要思想是按照边的权重(从小到大)处理它们，将边加入最小生成树中，
    加入的边不会与已经加入最小生成树的边构成环，直到树中含有V-1条边为止。
    '''

    def __init__(self, g: EdgeWeightedGraph):
        # 保存最小生成树的所有边
        self.mst = Queue()

        # 索引代表顶点，使用uf.connect(v,w)可以判断顶点v和顶点w是否在同一颗树中，
        # 使用uf.union(v,w)可以把顶点v所在的树和顶点w所在的树合并
        self.uf = UFTreeWeighted(g.v())

        # 存储图中所有的边，使用最小优先队列，对边按照权重进行排序
        self.pq = MinPriorityQueue(g.e() + 1)

        # 把图中所有的边存储到pq中
        e = g.get_all_edges()
        while True:
            tmp_e = e.dequeue()
            if tmp_e is False or tmp_e is None:
                break
            self.pq.insert(tmp_e)

        # 遍历pq队列，拿到最小权重的边，进行处理
        while not self.pq.is_empty() and self.mst.size() < g.v() - 1:
            # 找到权重最小的边
            t_min = self.pq.delete_min()
            # 找到该边的两个顶点
            v = t_min.either()
            w = t_min.other(v)

            # 判断这两个顶点是否已经在同一颗树中，如果在同一颗树中，则不对该边做处理，
            # 如果不在一棵树中，则让这两个顶点属于的两棵树合并成一棵树
            if self.uf.connected(v, w):
                continue

            self.uf.union(v, w)

            # 让边e进入到mst队列中
            self.mst.enqueue(t_min)

    def edges(self):
        '''获取最小生成树的所有边'''
        return self.mst
