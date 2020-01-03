# Singly Linked List

class Node(object):
	def __init__(self,val):
		self.val=val
		self.nextnode=None


a=Node('1')
b=Node('kumar')
c=Node('manish')
a.nextnode=b
b.nextnode=c
 

print a.val
print a.nextnode.val
print a.nextnode.nextnode.val
