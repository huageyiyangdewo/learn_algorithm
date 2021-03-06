from graph.kruskal_mst import KruskalMST
from graph.edge import Edge
from graph.edge_weight_graph import EdgeWeightedGraph

'''
8
16
4 5 0.35
4 7 0.37
5 7 0.28
0 7 0.16
1 5 0.32
0 4 0.38
2 3 0.17
1 7 0.19
0 2 0.26
1 2 0.36
1 3 0.29
2 7 0.34
6 2 0.40
3 6 0.52
6 0 0.58
6 4 0.93
'''
g = EdgeWeightedGraph(8)
e = Edge(4, 5, 0.35)
g.add_edge(e)
e = Edge(4, 7, 0.37)
g.add_edge(e)
e = Edge(5, 7, 0.28)
g.add_edge(e)
e = Edge(0, 7, 0.16)
g.add_edge(e)
e = Edge(1, 5, 0.32)
g.add_edge(e)
e = Edge(0, 4, 0.38)
g.add_edge(e)
e = Edge(2, 3, 0.17)
g.add_edge(e)
e = Edge(1, 7, 0.19)
g.add_edge(e)
# e = Edge(0, 4, 0.38)
# g.add_edge(e)
# e = Edge(1, 7, 0.19)
# g.add_edge(e)
e = Edge(0, 2, 0.26)
g.add_edge(e)
e = Edge(1, 2, 0.36)
g.add_edge(e)
e = Edge(1, 3, 0.29)
g.add_edge(e)
e = Edge(2, 7, 0.34)
g.add_edge(e)
e = Edge(6, 2, 0.40)
g.add_edge(e)
e = Edge(3, 6, 0.52)
g.add_edge(e)
e = Edge(6, 0, 0.58)
g.add_edge(e)
e = Edge(6, 4, 0.93)
g.add_edge(e)


# 创建一个KruskalMST对象，计算加权无向图中的最小生成树
prim_mst = KruskalMST(g)
edges = prim_mst.edges()

while True:
    e = edges.dequeue()
    if e is False or e is None:
        break
    v = e.either()
    w = e.other(v)
    print('边:{},权重{}'.format((str(v) + '-' + str(w)), e.weight()))

'''
边:0-7,权重0.16
边:2-3,权重0.17
边:1-7,权重0.19
边:0-2,权重0.26
边:5-7,权重0.28
边:4-5,权重0.35
边:6-2,权重0.4
'''