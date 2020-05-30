from stack.stack_link import StackLink


class DepthFirstPaths(object):
    '''深度优先之路径查找'''

    def __init__(self, g, s):
        '''构造深度优先搜索对象，使用深度优先搜索找出G图中起点为s的所有路径'''

        # 索引代表顶点，值表示当前顶点是否已经被搜索
        self.marked = [None] * g.get_v()

        # 记录有多少个顶点与s顶点相通
        self.count = 0

        # 索引代表顶点，值代表从起点s到当前顶点路径上的最后一个顶点
        self.edge_to = [None] * g.get_v()

        self.s = s
        self.dfs(g, s)

    def dfs(self, g, v):
        '''使用深度优先搜索找出G图中v顶点的所有相邻顶点'''

        # 把v表示为已搜索
        self.marked[v] = True

        # 遍历顶点v的邻接表，拿到每一个相邻的顶点，继续递归搜索
        w = g.get_adj(v).dequeue()
        while w is not False:
            # 如果顶点w没有被搜索，则继续递归搜索
            if not self.marked[w]:
                self.edge_to[w] = v  # 到达顶点w的路径上的最后一个顶点是v
                self.dfs(g, w)
            else:
                w = g.get_adj(v).dequeue()

        # 相通顶点数量 + 1
        self.count += 1

    def has_path_to(self, w):
        '''判断w顶点与s顶点是否相通'''
        return True if self.marked[w] is True else False

    def path_to(self, v):
        '''找出从起点s到顶点v的路径(就是该路径经过的顶点)'''
        if not self.has_path_to(v):
            return None

        # 创建栈对象，保存路径中的所有顶点
        path = StackLink()
        path.push(v)

        # 通过循环，从顶点v开始，一直往前找，到找到起点为止
        while True:
            tmp = self.edge_to[v]
            if tmp == self.s:
                path.push(self.s)
                break
            path.push(tmp)
            v = tmp

        return path


