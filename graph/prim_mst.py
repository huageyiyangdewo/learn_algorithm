from queue_l.queue_link import Queue
from priority.index_min_priority_queue import IndexMinPriorityQueue
from graph.edge_weight_graph import EdgeWeightedGraph
import math


class PrimMST(object):
    '''
    Prim算法
    切分规则：把最小生成树中的顶点看做是一个集合，把不在最小生成树中的顶点看做是另外一个集合。
    '''

    def __init__(self, g):
        # 根据一副加权无向图，创建最小生成树计算对象

        # 索引代表顶点，值表示当前顶点和最小生成树之间的最短边
        self.edge_to = [None] * g.v()
        # 索引代表顶点，值表示当前顶点和最小生成树之间的最短边的权重 默认无穷大
        self.dist_to = [float('inf')] * g.v()
        # 索引代表顶点，如果当前顶点已经在树中，则值为true，否则为false
        self.marked = [None] * g.v()
        # 存放树中顶点与非树中顶点之间的有效横切边
        self.pq = IndexMinPriorityQueue(g.v())

        # 默认让顶点0进入到树中，但是树中只有一个顶点0，
        # 因此，0顶点默认没有和其他的顶点相连，所以让distTo对应位置处的值存储0.0
        self.dist_to[0] = 0.0
        self.pq.insert(0, 0.0)

        # 遍历索引最小优先队列，拿到最小和N切边对应的顶点，把该顶点加入到最小生成树中
        while not self.pq.is_empty():
            self.visit(g, self.pq.delete_min())

    def visit(self, g: EdgeWeightedGraph, v: int):
        '''将顶点v添加到最小生成树中，并且更新数据'''

        # 把顶点v添加到最小生成树中
        self.marked[v] = True

        # 更新数据
        while True:
            e = g.adj(v).dequeue()
            if e is False or e is None:
                break
            # 获取e边的另外一个顶点(当前顶点是v)
            w = e.other(v)
            # 判断另外一个顶点是不是已经在树中，如果在树中，则不做任何处理，如果不再树中，更新数据
            if self.marked[w]:
                continue
            # 判断边e的权重是否小于从w顶点到树中已经存在的最小边的权重；
            if math.isinf(self.dist_to[w]) or self.dist_to[w] > e.weight():
                self.edge_to[w] = e
                self.dist_to[w] = e.weight()

                e_weight = e.weight()
                if self.pq.contains(w):
                    self.pq.change_item(w, e_weight)
                else:
                    self.pq.insert(w, e_weight)

    def edges(self):
        '''获取最小生成树的所有边'''
        # 创建队列对象
        all_edges = Queue()
        # 遍历edgeTo数组，拿到每一条边，如果不为null，则添加到队列中
        for i in range(len(self.edge_to)):
            if self.edge_to[i] is not None:
                all_edges.enqueue(self.edge_to[i])
        return all_edges
