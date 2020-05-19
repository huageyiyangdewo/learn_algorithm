from queue.queue_link import Queue


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.size())
# print(q._head.item)
# print(q._last.item)
print(q.dequeue())
print(q.dequeue())

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.size())
print(q._last)
print(q._head)