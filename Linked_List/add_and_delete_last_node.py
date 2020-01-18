# Add and Delete Last Node in a linked list



class Node:
	def __init__(self,val):
		self.value = val
		self.next = None



class LinkedList:
    def __init__(self):
	    self.head = None
	    self.tail = None


def printallnodeval(llist):
	temp=llist.head
	while temp:
		print temp.value
		temp=temp.next
	return 


def DeleteNode(head):
	temp=head
	while temp.next.next:
		temp=temp.next
	temp.next=None
	return head



def InserteNode(head,tail,value):
	temp=Node(value)
	tail.next=temp
	return head




# Creating Node
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

llist=LinkedList()
llist.head = a 
llist.tail = e

printallnodeval(llist)

print 'after addition of Node'

llist.head=InserteNode(llist.head,llist.tail,10)

printallnodeval(llist)


print 'Delete Node from tail of the linked list'

llist.tail=DeleteNode(llist.head)

printallnodeval(llist)
