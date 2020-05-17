from linear.singlelinklist import SingleNode, SingleLinkList
from linear.cyclelinkcheck import CycleLinkCheck


a = SingleNode('a')
b = SingleNode('b')
c = SingleNode('c')
d = SingleNode('d')
e = SingleNode('e')
f = SingleNode('f')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = c

s_link = SingleLinkList(a)

print(CycleLinkCheck.is_cycle(s_link))
h = CycleLinkCheck.get_entrance(s_link)
print(h.item)
