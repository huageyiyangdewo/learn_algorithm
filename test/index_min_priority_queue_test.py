from priority.index_min_priority_queue import IndexMinPriorityQueue


q = IndexMinPriorityQueue(10)

q.insert(0, 'A')
q.insert(1, 'C')
q.insert(2, 'F')
q.insert(3, 'B')
q.insert(4, 'D')
q.insert(5, 'E')
q.insert(6, 'G')

# q.change_item(2, 'B')

print(q.delete(0))


while True:
    t = q.delete_min()
    if t is not None:
        print(t, end=' ')
    else:
        break
