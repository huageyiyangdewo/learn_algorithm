from priority.min_priority_queue import MinPriorityQueue


q = MinPriorityQueue(40)
for i in range(19, -12, -1):
    q.insert(i)
# q.insert(-2)
# q.insert(-4)
# q.insert(-7)

print(q.item)
while True:
    ret = q.delete_min()
    if ret is None:
        break
    print(ret, end=' ')
