from graph.directedcycle import DirectedCycle
from graph.digraph import DiGraph


g = DiGraph(13)

g.add_edge(0, 5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 6)
g.add_edge(3, 5)
g.add_edge(5, 4)
g.add_edge(4, 3)
# g.add_edge(4, 6)

g.add_edge(7, 8)

# g.add_edge(9, 11)
# g.add_edge(9, 10)
# g.add_edge(9, 12)
# g.add_edge(11, 12)

# 准备深度优先搜索对象
s = DirectedCycle(g)
print(s.has_cycle())
