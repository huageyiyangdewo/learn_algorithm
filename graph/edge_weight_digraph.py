from queue_l.queue_link import Queue


class EdgeWeightedDiGraph(object):
    '''创建一个含有V个顶点的空加权有向图'''

    def __init__(self, v):
        # 初始化顶点数量
        self._v = v
        # 初始化边的数量
        self._e = 0
        # 初始化邻接表
        self._adj = [Queue() for i in range(v)]

    def v(self):
        '''获取图中顶点的数量'''
        return self._v

    def e(self):
        '''获取图中边的数量'''
        return self._e

    def add_edge(self, e):
        '''向加权无向图中添加一条边e'''
        # 边e是有方向的，所以只需要让e出现在起点的邻接表中即可
        v = e.from_v()

        self._adj[v].enqueue(e)
        # 边数量+1
        self._e += 1

    def adj(self, v):
        '''获取和顶点v关联的所有边'''
        return self._adj[v]

    def get_all_edges(self):
        '''获取加权有向图的所有边'''
        # 创建一个队列对象，存储所有的边
        all_edges = Queue()
        # 遍历图中的每一个顶点，得到该顶点的邻接表，遍历得到每一条边，添加到队列中返回即可
        for i in range(self._v):
            t_q = self.adj(i)

            # 遍历v顶点的邻接表，找到每一条和v关联的边
            t_e = t_q.dequeue()
            while t_e is not False:
                all_edges.enqueue(t_e)

                t_e = t_q.dequeue()

        return all_edges


