from graph.topo_logical import ToPoLogical
from graph.digraph import DiGraph


di_graph = DiGraph(6)
di_graph.add_edge(0, 2)
di_graph.add_edge(0, 3)
di_graph.add_edge(2, 4)
di_graph.add_edge(3, 4)
di_graph.add_edge(4, 5)
di_graph.add_edge(1, 3)

order = ToPoLogical(di_graph)

t_order = order.get_order()

path = ''
while True:
    t = t_order.pop()
    if t is None:
        break
    if path:
        path += ('->' + str(t))
    else:
        path = str(t)

print(path)


