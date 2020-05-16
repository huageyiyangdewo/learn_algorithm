from linear.doublelinklist import DoubleLinkList

ll = DoubleLinkList()
ll.add(1)
ll.add(2)
ll.append(2)
ll.insert(2, 6)
# ll.insert(1, 3)
# ll.remove(3)
ll.travel()
ll.remove(2)
ll.travel()
print(ll.get(2))
# print(ll.length())