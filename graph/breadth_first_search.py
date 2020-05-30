from queue_l.queue_link import Queue

class BreadthFirstSearch(object):
    '''广度优先搜索'''

    def __init__(self, g, s):
        '''构造广度优先搜索对象，使用广度优先搜索找出G图中s顶点的所有相邻顶点'''

        # 索引代表顶点，值表示当前顶点是否已经被搜索
        self.marked = [None] * g.get_v()

        # 记录有多少个顶点与s顶点相通
        self.count = 0

        # 用来存储待搜索邻接表的点
        self.wait_search = Queue()

        self.bfs(g, s)

    def bfs(self, g, v):
        '''使用广度优先搜索找出G图中v顶点的所有相邻顶点'''

        # 把v表示为已搜索
        self.marked[v] = True
        # 让顶点v进入队列，待搜索
        self.wait_search.enqueue(v)
        # 通过循环，如果队列不为空，则从队列中弹出一个待搜索的顶点进行搜索
        while not self.wait_search.is_empty():
            # 弹出一个待搜索的顶点
            tmp = self.wait_search.dequeue()

            # 遍历顶点v的邻接表，拿到每一个相邻的顶点，继续递归搜索
            w = g.get_adj(tmp).dequeue()
            while w is not False:
                # 如果顶点w没有被搜索，则继续递归搜索
                if not self.marked[w]:
                    self.bfs(g, w)
                w = g.get_adj(v).dequeue()

        # 相通顶点数量 + 1
        self.count += 1

    def get_marked(self, w):
        '''判断w顶点与s顶点是否相通'''
        return True if self.marked[w] is True else False

    def get_count(self):
        '''获取与顶点s相通的所有顶点的总数'''
        return self.count


