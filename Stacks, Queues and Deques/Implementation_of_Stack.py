#Stack Implementation

class Stack:
	def __init__(self):
		self.item=[]

	def push(self,n):
		self.item.append(n)
	def pop(self):
		return self.item.pop()
	def peek(self):
		return self.item[len(self.item)-1]
	def isempty(self):
		return self.item==[]
	def size(self):
		return len(self.item)


s=Stack()
print s.isempty()
s.push(3)
s.push('manish')
print s.peek()
s.push(True)
print s.size()
print s.isempty()
print s.pop()
print s.pop()
print s.size()
print s.pop()
print s.isempty()
