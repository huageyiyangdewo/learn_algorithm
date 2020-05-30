class DirectedCycle(object):
    '''拓扑排序--检查有向环'''

    def __init__(self, g):
        # 记录图中是否有环
        self.has_cycle_abt = False
        # 索引代表顶点，值表示当前顶点是否已经被搜索
        self.marked = [None] * g.get_v()
        # 索引代表顶点，使用栈的思想，记录当前顶点有没有已经处于正在搜索的有向路径上
        self.on_stack = [None] * g.get_v()

        # 找到图中每一个顶点，让每一个顶点作为入口，调用一次dfs进行搜索
        for i in range(g.get_v()):
            # 判断如果当前顶点还没有搜索过，则调用dfs进行搜索
            if not self.marked[i]:
                self.dfs(g, i)

    def has_cycle(self):
        '''判断当前有向图G中是否有环'''
        return self.has_cycle_abt

    def dfs(self, g, v):
        '''基于深度优先搜索，检测图G中是否有环'''

        # 把v表示为已搜索
        self.marked[v] = True
        # 把当前顶点进栈
        self.on_stack[v] = True

        # 遍历顶点v的邻接表，拿到每一个相邻的顶点，继续递归搜索
        w = g.get_adj(v).dequeue()
        while w is not False:
            # 如果顶点w没有被搜索，则继续递归搜索
            if not self.marked[w]:
                self.dfs(g, w)

            # 判断当前顶点w是否已经在栈中，如果已经在栈中，证明当前顶点之前处于正在搜索的状态，
            # 那么现在又要搜索一次，证明检测到环了
            if self.on_stack[w]:
                self.has_cycle_abt = True
                return True

            w = g.get_adj(v).dequeue()

        # 把当前顶点出栈
        self.on_stack[v] = False

