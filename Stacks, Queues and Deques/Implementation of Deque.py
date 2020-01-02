# Implementation of Deque

class Deque:
	def __init__(self):
		self.item=[]
	def addfront(self,num):
		self.item.append(num)
	def addrear(self,num):
		self.item.insert(0,num)
	def removefront(self):
		return self.item.pop()
	def removerear(self):
		return self.item.pop(0)
	def isempty(self):
		return self.item==[]
	def size(self):
		return len(self.item)

d = Deque()
d.addfront('manish')
d.addrear('kumar')
print d.size()
print d.isempty()
print d.removefront()+' '+d.removerear()


