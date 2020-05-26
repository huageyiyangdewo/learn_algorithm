from uf.uf_tree_weighted import UFTreeWeighted


uf = UFTreeWeighted(5)
print('默认清楚的分组:{}'.format(uf.count()))
while True:

    p = input('输入要合并的元素p:')
    p = int(p)
    q = input('输入要合并的元素q:')
    q = int(q)

    if uf.connected(p, q):
        print('%d - %d 已结在同一分组中了' % (p, q))

    uf.union(p, q)
    print('当前的分组个数:{}'.format(uf.count()))
