from queue_l.queue_link import Queue


class Graph(object):

    def __init__(self, v):
        # 顶点数目
        self.v = v
        # 边的数量
        self.e = 0
        # 邻接表
        self.adj = [Queue()] * n

    def get_v(self):
        '''获取顶点数目'''
        return self.v

    def get_e(self):
        '''获取边的数目'''
        return self.e

    def add_edge(self, v, w):
        '''向图中添加一条边 v-w'''
        # 在无向图中，边是没有方向的，所以该边既可以说是从v到w的边，又可以说是从w到v的边，
        # 因此，需要让w出现在v的邻接表中，并且还要让v出现在w的邻接表中
        self.adj[v].enqueue(w)
        self.adj[w].enqueue(v)

        self.e += 1

    def get_adj(self, v):
        '''获取和顶点v相邻的所有顶点'''
        return self.adj[v]
