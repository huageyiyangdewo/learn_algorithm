from tree.red_black_tree import RedBlackTree


t = RedBlackTree()
t.put(1, '1')
t.put(2, '2')
t.put(3, '3')
t.put(4, '4')
t.put(5, '5')

i = 1
while True:

    ret = t.get(i)
    print(ret)
    if ret is None:
        break
    i += 1