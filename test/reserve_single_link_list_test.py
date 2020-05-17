from linear.singlelinklist import SingleLinkList
from linear.reserve_single_link_list import ReserveSingleLinkList

ll = SingleLinkList()
ll.add(1)
ll.insert(0, 2)
ll.insert(1, 3)
ll.travel()
# print(ll.length())
print('*' * 10)

# b = ReserveSingleLinkList.reserve_by_head_add(ll)
b = ReserveSingleLinkList.reserve_by_3_pointer(ll)
b.travel()
# print(b.item)
# print(b.next.item)
# print(b.next.next.item)