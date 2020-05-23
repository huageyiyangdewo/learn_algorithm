from priority.max_priority_queue import MaxPriorityQueue


q = MaxPriorityQueue(40)
for i in range(19, -12, -1):
    q.insert(i)

while True:
    ret = q.delete_max()
    if ret is None:
        break
    print(ret, end=' ')
    