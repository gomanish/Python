#  Singly Linked List Cycle Check 

''' Given a singly linked list, write a function which takes in the first node
in a singly linked list and returns a boolean indicating if the linked list 
contains a cycle '''

class Node(object):
	def __init__(self,num):
		self.num=num
		self.nextnode=None


def cycle_check(node):
	runner1=node
	runner2=node

	while runner2!=None and runner2.nextnode!=None:
		runner1=runner1.nextnode
		runner2=runner2.nextnode.nextnode
		if runner2==runner1:
			return True

	return False



a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)


#creating circular linked list

a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=a


x=Node('man')
y=Node('manish')
z=Node('kumar')

#creating non circular linked list

x.nextnode=y
y.nextnode=z


# Cheacking for circular linked list
print(cycle_check(a))

# cheacking for non circular linked list
print(cycle_check(x))
