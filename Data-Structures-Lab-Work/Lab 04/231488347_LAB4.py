from queue import Empty


class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def stack_check(self):
        return self._data


##TASK 2
def signature_transfer(s, t):
    while s.is_empty() is not True:
        t.push(s.pop())

print("TASK 2")

st1 = ArrayStack()
st2 = ArrayStack()
for numbers in range(10):
    st1.push(numbers)
    st2.push(numbers+2)
print(st1.stack_check(),st2.stack_check())
signature_transfer(st1,st2)
print(st1.stack_check(),st2.stack_check())
                     


##TASK 3
def list_reverse(l):
    reverse_stack = ArrayStack()
    for i in range(0, len(l)):
        reverse_stack.push(l[i])

    l = []
    while reverse_stack.is_empty() is not True:
        l.append(reverse_stack.pop())
    return l
print("\nTASK 3")

print(list_reverse([1,2,3,4,5]))
    

##TASK 4
test_stack = ArrayStack()
temp_stack1 = ArrayStack()
temp_stack2 = ArrayStack()

for i in range(10):
    test_stack.push(i)

print("\nTASK 4")
print(test_stack.stack_check())

signature_transfer(test_stack, temp_stack1)
signature_transfer(temp_stack1, temp_stack2)
signature_transfer(temp_stack2, test_stack)

print(test_stack.stack_check())

# TASK 5
def postfix_calc(eq):
    num_stack = ArrayStack()
    eq = eq.split(" ")

    for i in range(0, len(eq)):

        if eq[i].isdigit() is True:
            num_stack.push(eq[i])

        else:
            n1 = int(num_stack.pop())
            n2 = int(num_stack.pop())
            op = eq[i]

            if op == "+":
                num_stack.push(n2 + n1)
            if op == "-":
                num_stack.push(n2 - n1)
            if op == "*":
                num_stack.push(n2 * n1)
            if op == "/":
                num_stack.push(n2 / n1)

    return num_stack.top()

print("\nTASK 5")
print(postfix_calc("5 2 + 8 3 - * 4 /"))
