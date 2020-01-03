# Doubly Linked List

class Node(object):
	def __init__(self,val):
		self.val=val
		self.next_node=None
		self.prev_node=None


a=Node(1)
b=Node('manish')
c=Node('kumar')
d=Node('mayank')

a.next_node=b
b.prev_node=a
c.next_node=d
c.prev_node=b
d.prev_node=c

print a.val
print d.prev_node.prev_node.val
