from linear.singlecyclelinklist import SingleCycleLinkList

l_t = SingleCycleLinkList()

l_t.add(1)
l_t.add(2)
l_t.insert(0, 2)
l_t.insert(1, 3)
l_t.remove(3)
l_t.travel()
# print(l_t.length())
print(l_t.get(1))