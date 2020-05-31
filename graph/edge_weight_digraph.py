from queue_l.queue_link import Queue


class EdgeWeightedGraph(object):
    '''创建一个含有V个顶点的空加权无向图'''

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
        # 需要让边e同时出现在e这个边的两个顶点的邻接表中
        v = e.either()
        w = e.other(v)

        self._adj[v].enqueue(e)
        self._adj[w].enqueue(e)
        # 边数量+1
        self._e += 1

    def adj(self, v):
        '''获取和顶点v关联的所有边'''
        return self._adj[v]

    def get_all_edges(self):
        '''获取加权无向图的所有边'''
        # 创建一个队列对象，存储所有的边
        all_edges = Queue()
        # 遍历图中的每一个顶点，找到该顶点的邻接表，邻接表中存储了该顶点关联的每一条边
        # 因为这是无向图，所以同一条边同时出现在了它关联的两个顶点的邻接表中，需要让一条边只记录一次；
        for i in range(self._v):
            t_q = self.adj(i)

            # 遍历v顶点的邻接表，找到每一条和v关联的边
            t_e = t_q.dequeue()
            while t_e is not False:
                # 因为是从0开始，所以这样便可以剔除掉重复的边
                if t_e.other(i) < i:
                    all_edges.enqueue(t_e)

                t_e = t_q.dequeue()

        return all_edges


