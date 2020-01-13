# Tree Representation and implementztion through list


def BinaryTree(r):
	return [r,[],[]]

def Insertleft(root,newbeanch):
	t=root.pop(1)
	if len(t)>1:
		root.insert(1,[newbeanch,t,[]])
	else:
		root.insert(1,[newbeanch,[],[]])
	return root

def Insertright(root,newbeanch):
	t=root.pop(2)
	if len(t)>1:
		root.insert(2,[newbeanch,[],t])
	else:
		root.insert(2,[newbeanch,[],[]])
	return root



def getrootval(root):
	return root[0]


def setrootval(root,value):
	root[0]=value

def getleftchild(root):
	return root[1]

def getrightchild(root):
	return root[2]


r=BinaryTree(2)

print r
Insertright(r,3)
Insertleft(r,4)
Insertleft(r,5)
Insertright(r,6)
print r
print 'Set New Root Value : ',
setrootval(r,1)
print r

print 'Get root value : ',
print getrootval(r)

print 'Get Left Child : ',
print getrightchild(r)

print 'Get Right Child : ',
print getrightchild(r)
