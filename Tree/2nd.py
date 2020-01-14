# Binary tree implementation using node and references 


class BinartTree(object):
	def __init__(self,rootobject):
		self.key=rootobject
		self.leftchild=None
		self.rightchild=None
	

	def insertleft(self,value):
		if self.leftchild==None:
			self.leftchild=BinartTree(value)
		else:
			t=BinartTree(value)
			t.leftchild=self.leftchild
			self.leftchild=t



	def insertright(self,value):
		if self.rightchild==None:
			self.rightchild=BinartTree(value)
		else:
			t=BinartTree(value)
			t.rightchild=self.rightchild
			self.rightchild=t


	def getrightchild(self):
		return self.rightchild

	def getleftchild(self):
		return self.leftchild

	def setrootvalue(self,value):
		self.key=value

	def getrootvalue(self):
		return self.key


r=BinartTree(3)
r.insertright(2)
r.insertright(1)
r.insertleft(4)
r.insertleft(5)
print r.getrootvalue()
print r.getleftchild().key
print r.getrightchild().key
r.setrootvalue(10)
print r.getrootvalue()
