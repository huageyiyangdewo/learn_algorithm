from stack.stack_link import StackLink


class DepthFirstOrder(object):
    '''顶点排序'''

    def __init__(self, g):
        # 索引代表顶点，值表示当前顶点是否已经被搜索
        self.marked = [None] * g.get_v()
        # 使用栈，存储顶点序列
        self.reserve_post = StackLink()

        # 遍历图中的每一个顶点，让每个顶点作为入口，完成一次深度优先搜索
        for i in range(g.get_v()):
            # 判断如果当前顶点还没有搜索过，则调用dfs进行搜索
            if not self.marked[i]:
                self.dfs(g, i)

    def dfs(self, g, v):
        '''基于深度优先搜索，把顶点排序'''

        # 把v表示为已搜索
        self.marked[v] = True

        # 遍历顶点v的邻接表，拿到每一个相邻的顶点，继续递归搜索
        w = g.get_adj(v).dequeue()
        while w is not False:
            # 如果顶点w没有被搜索，则继续递归搜索
            if not self.marked[w]:
                self.dfs(g, w)

            w = g.get_adj(v).dequeue()

        # 让顶点v进栈
        self.reserve_post.push(v)

    def get_reverse_post(self):
        '''获取顶点线性序列'''
        return self.reserve_post

