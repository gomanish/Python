# Implement a Queue - Using Two Stacks

class Queue2Stacks:
	
	def __init__(self):
		self.stack1=[]
		self.stack2=[]
	
	def enqueue(self,num):
		self.stack1.append(num)
	
	def dequeue(self):
		for i in range(0,len(self.stack1)):
			self.stack2.append(self.stack1.pop())
		return self.stack2.pop()


q = Queue2Stacks()
q.enqueue('manish')
q.enqueue('kumar')
q.enqueue(True)
print q.dequeue()
print q.dequeue()
