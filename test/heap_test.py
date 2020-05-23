from heap.heap import Heap

h = Heap(10)
h.insert('A')
h.insert('B')
h.insert('C')
h.insert('D')
h.insert('E')
h.insert('F')
h.insert('G')

while True:
    ret = h.delete_max()
    if ret is None:
        break
    print(ret, end=' ')


