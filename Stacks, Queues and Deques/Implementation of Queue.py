# Implementation of Queue

class queue:
	def __init__(self):
		self.item=[]
	def enqueue(self,m):
		self.item.insert(0,m)
	def dequeue(self):
		return self.item.pop()
	def  isempty(self):
		return self.item==[]
	def size(self):
		return len(self.item)


s=queue()
print s.size()
print s.isempty()
s.enqueue(2)
s.enqueue('manish')
s.enqueue('kumar')
print s.dequeue()
print s.dequeue()
