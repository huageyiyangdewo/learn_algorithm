from graph.dijkstraSP import DijkstraSP
from graph.directed_edge import DirectedEdge
from graph.edge_weight_digraph import EdgeWeightedDiGraph

'''
8
15
4 5 0.35
5 4 0.35
4 7 0.37
5 7 0.28
7 5 0.28
5 1 0.32
0 4 0.38
0 2 0.26
7 3 0.39
1 3 0.29
2 7 0.34
6 2 0.40
3 6 0.52
6 0 0.58
6 4 0.93
'''
g = EdgeWeightedDiGraph(8)
e = DirectedEdge(4, 5, 0.35)
g.add_edge(e)
e = DirectedEdge(5, 4, 0.35)
g.add_edge(e)
e = DirectedEdge(4, 7, 0.37)
g.add_edge(e)
e = DirectedEdge(5, 7, 0.28)
g.add_edge(e)
e = DirectedEdge(7, 5, 0.28)
g.add_edge(e)
e = DirectedEdge(5, 1, 0.32)
g.add_edge(e)
e = DirectedEdge(0, 4, 0.38)
g.add_edge(e)
e = DirectedEdge(0, 2, 0.26)
g.add_edge(e)
e = DirectedEdge(7, 3, 0.39)
g.add_edge(e)
e = DirectedEdge(1, 3, 0.29)
g.add_edge(e)
e = DirectedEdge(2, 7, 0.34)
g.add_edge(e)
e = DirectedEdge(6, 2, 0.40)
g.add_edge(e)
e = DirectedEdge(3, 6, 0.52)
g.add_edge(e)
e = DirectedEdge(6, 0, 0.58)
g.add_edge(e)
e = DirectedEdge(6, 4, 0.93)
g.add_edge(e)


# 创建一个DijkstraSP对象，计算加权无向图中的最小生成树
prim_mst = DijkstraSP(g, 0)
# 查找最短路径,0->6的最短路径
edges = prim_mst.path_to(6)

path = ''
while not edges.is_empty():
    e = edges.dequeue()
    print('from:{}-->to:{}, weight:{}'.format(str(e.from_v()), str(e.to()), e.weight()))

'''
from:3-->to:6, weight:0.52
from:7-->to:3, weight:0.39
from:2-->to:7, weight:0.34
from:0-->to:2, weight:0.26
'''
