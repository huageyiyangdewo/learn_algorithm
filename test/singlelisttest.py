from linear.singlelinklist import SingleLinkList

ll = SingleLinkList()
ll.add(1)
ll.insert(0, 2)
ll.insert(1, 3)
ll.remove(3)
ll.travel()
# print(ll.length())
print(ll.get(1))