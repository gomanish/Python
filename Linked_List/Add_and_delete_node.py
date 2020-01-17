# Add and Delete a node from head in a linked list



class Node:
	def __init__(self,val):
		self.value = val
		self.next = None



class LinkedList:
    def __init__(self):
	    self.head = None
	    self.tail = None



def insertNode(head,data):
	temp = Node(data)
	temp.next = head
	head=temp
	return head



def deleteNode(head):
	temp=head.next        # It takes Head of the Linked List
	head=temp
	return head

def printallnodeval(llist):
	temp=llist.head
	while temp:
		print temp.value
		temp=temp.next
	return 

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

print 'After delete Head of the Linked List'

llist.head = deleteNode(llist.head)
printallnodeval(llist)

print 'After Addition of a Node'
llist.head = insertNode(llist.head,10)
printallnodeval(llist)
