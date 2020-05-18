from stack.stack_sequence import StackSequence
from stack.stack_link import StackLink

s = StackLink()
print(s.is_empty())
s.push(1)
s.push(2)
s.push(3)
s.push(4)

a = s.pop()
b = s.pop()
c = s.pop()
d = s.pop()
print(a, b, c, d, sep=',')
# print(a, b, sep=',')