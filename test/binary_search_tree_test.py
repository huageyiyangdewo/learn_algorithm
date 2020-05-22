from tree.binary_search_tree import Node, BinarySearchTree


new_tree = BinarySearchTree()
new_tree.insert('E', 'E')

new_tree.insert('B', 'B')

new_tree.insert('G', 'G')
new_tree.insert('A', 'A')
new_tree.insert('D', 'D')
new_tree.insert('F', 'F')
new_tree.insert('H', 'H')
new_tree.insert('C', 'C')

print(new_tree.size())

# print(new_tree.get(2))

# print(new_tree.delete(10))
print(new_tree.size())
# print(new_tree.get(10))
print(new_tree.min())
print(new_tree.max())
print('--------------')
keys_que = new_tree.pre_ergodic()
for i in keys_que:
    print(i.item.value)

print('==============')
keys_que = new_tree.mid_ergodic()
for i in keys_que:
    print(i.item.value)

print('1111111111111111')
keys_que = new_tree.suf_ergodic()
for i in keys_que:
    print(i.item.value)


print('2222222222')
keys_que = new_tree.layer_ergodic()
for i in keys_que:
    print(i.item.value)

print('888888888888888')
print(new_tree.max_depth())