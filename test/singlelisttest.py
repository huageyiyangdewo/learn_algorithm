from linear.singlelinklist import SingleLinkList

ll = SingleLinkList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.insert(0, 2)
ll.insert(1, 3)
# ll.remove(3)
ll.travel()
# print(ll.length())
# print(ll.get(1))
print('-' * 10)

ll.reserve()

ll.travel()