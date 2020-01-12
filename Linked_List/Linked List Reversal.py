# Linked List Reversal

class Node(object):
	def __init__(self,num):
		self.num=num
		self.nextnode=None


def reverse(node):
	current=node
	previous=None
	nextnode = None
	while current:
		nextnode=current.nextnode
		current.nextnode=previous
		previous=current
		current=nextnode

	return

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)


a.nextnode=b
b.nextnode=c
c.nextnode=d

print 'Before reverse'
print a.nextnode.num
print b.nextnode.num
print c.nextnode.num
print '\n'


reverse(a)

print 'After reverse'
print d.nextnode.num
print c.nextnode.num
print b.nextnode.num

