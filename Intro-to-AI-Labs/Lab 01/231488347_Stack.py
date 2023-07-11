		
# Custom stack implementation in Python
class LIFO_Stack:

	# Constructor to initialize the stack
	def __init__(self, size):
		self.arr = [None] * size
		self.capacity = size
		self.top = -1
		
	# Function to add an element `val` to the stack
	def push(self, val):
		if self.isFull():
			print('Stack Overflow!! Calling exit()…')
			exit(-1)
			
		print(f'Inserting {val} into the stack…')
		self.top = self.top + 1
		self.arr[self.top] = val
		
	# Function to pop a top element from the stack
	def pop(self):
		# check for stack underflow
		if self.isEmpty():
			print('Stack Underflow!! Calling exit()…')
			exit(-1)
		print(f"Removing {self.peek()} from the stack")
		
		# decrease stack size by 1 and (optionally) return the popped element
		top = self.arr[self.top]
		self.arr[self.top] = None
		self.top = self.top - 1	

	def peek(self):
		return self.arr[self.top]
		
	def size(self):
		
		if self.isFull():
			return self.capacity
		else:
			i,count = 0,0
			while self.arr[i] is not None:
				count += 1
				i +=1
			return count
			
		
	def isEmpty(self):
		if self.arr[self.top] is None:
			return True
		else:
			return False
		
	def isFull(self):
		if None not in self.arr:
			return True
		else:
			return False
			
if __name__ == '__main__':
	stack = LIFO_Stack(3)
	
	stack.push(1)
	stack.push(2)
	
	stack.pop()
	stack.pop()
	
	stack.push(3)
	
	print("Top element is, ", stack.peek())
	print("The stack size is, ", stack.size())
	
	if stack.isEmpty():
		print("Stack is empty")
	else:
		print("Stack is not empty")
