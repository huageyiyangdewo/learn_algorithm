from tree.binary_search_tree import Node, BinarySearchTree


new_tree = BinarySearchTree()
new_tree.insert(10, '10')
new_tree.insert(9, '9')
new_tree.insert(4, '4')
new_tree.insert(6, '6')
new_tree.insert(17, '17')
new_tree.insert(12, '12')
new_tree.insert(13, '13')
new_tree.insert(11, '11')

print(new_tree.size())

print(new_tree.get(2))

print(new_tree.delete(10))
print(new_tree.size())
print(new_tree.get(10))
print(new_tree.min())
print(new_tree.max())