from queue_l.queue_link import Queue


class DiGraph(object):
    '''有向图'''

    def __init__(self, v):
        # 顶点数目
        self.v = v
        # 边的数量
        self.e = 0
        # 邻接表
        self.adj = [Queue() for i in range(v)]

    def get_v(self):
        '''获取顶点数目'''
        return self.v

    def get_e(self):
        '''获取边的数目'''
        return self.e

    def add_edge(self, v, w):
        '''向图中添加一条边 v->w'''
        # //只需要让顶点w出现在顶点v的邻接表中，因为边是有方向的，
        # 最终，顶点v的邻接表中存储的相邻顶点的含义是：  v->其他顶点
        self.adj[v].enqueue(w)

        self.e += 1

    def get_adj(self, v):
        '''获取和顶点v相邻的所有顶点'''
        return self.adj[v]

    def reserve(self):
        '''该图的反向图'''

        r = DiGraph(self.v)
        for v in range(self.v):
            # 获取由该顶点v指出的所有边

            w = self.get_adj(v).dequeue()
            while w is not False:
                r.add_edge(w, v)

        return r
