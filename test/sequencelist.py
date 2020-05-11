from linear.sequencelist import SequenceList

l_t = SequenceList()

l_t.append(1)
l_t.append(2)
l_t.append("你好")

l_t.insert(0, 8)

l_t.insert(2, 6)

print(l_t.get(1))

l_t.set(0, 9)

l_t.remove(3)

print(l_t.length())
print(l_t.is_full())
print(l_t.is_empty())
l_t.travel()