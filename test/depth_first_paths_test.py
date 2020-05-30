from graph.depth_first_paths import DepthFirstPaths
from graph.graph import Graph

'''
6 -- 6个顶点
8 -- 8条边
0 2
0 1
2 1
2 3
2 4
3 5
3 4
0 5
'''
g = Graph(6)

g.add_edge(0, 2)
g.add_edge(0, 1)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(0, 5)

# 准备深度优先路径查找
s = DepthFirstPaths(g, 0)

m1 = s.path_to(4)

path = ''
while True:
    t = m1.pop()
    if t is None:
        break
    if path:
        path += ('-' + str(t))
    else:
        path = str(t)

print(path)
