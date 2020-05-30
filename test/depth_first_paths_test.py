from graph.depth_first_search import DepthFirstSearch
from graph.graph import Graph


g = Graph(13)

g.add_edge(0, 5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 6)
g.add_edge(5, 3)
g.add_edge(5, 4)
g.add_edge(3, 4)
g.add_edge(4, 6)

g.add_edge(7, 8)

g.add_edge(9, 11)
g.add_edge(9, 10)
g.add_edge(9, 12)
g.add_edge(11, 12)

# 准备深度优先搜索对象
s = DepthFirstSearch(g, 0)
c = s.get_count()
print(c)

m1 = s.get_marked(1)
print(m1)

m7 = s.get_marked(8)
print(m7)
