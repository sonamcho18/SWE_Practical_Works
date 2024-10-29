class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.size())  # Should print 2

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.front())  # Should print 2
print(queue.size())  # Should print 2

def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Test the function
print(is_balanced("((()))"))  # Should print True
print(is_balanced("(()"))  # Should print False

def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test the function
print(reverse_string("Hello, World!"))  # Should print "!dlroW ,olleH"

def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

# Test the function
names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(names, 7))  # The winner's name will be printed

# Exercise 1
def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():  # if the token is a number
            stack.append(int(token))
        else:  # the token is an operator (+, -, *, /)
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    return stack.pop()

# Example usage
expression = "3 3 + 2 * 6 /"
result = evaluate_postfix(expression)
print(f"Result of evaluating postfix expression '{expression}': {result}")

# Exercise 2
def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():  # if the token is a number
            stack.append(int(token))
        else:  # the token is an operator (+, -, *, /)
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    return stack.pop()

# Example usage
expression = "3 3 + 2 * 6 /"
result = evaluate_postfix(expression)
print(f"Result of evaluating postfix expression '{expression}': {result}")

# Exercise 3
from collections import deque

class TaskScheduler:
    def __init__(self):
        self.queue = deque()
    
    def add_task(self, task):
        self.queue.append(task)
    
    def process_task(self):
        if self.queue:
            task = self.queue.popleft()
            print(f"Processing task: {task}")
        else:
            print("No tasks to process")

# Example usage
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")

scheduler.process_task()  
scheduler.process_task()  
scheduler.process_task()  
scheduler.process_task()  # Should print "No tasks to process"

# Exercise 4
from collections import deque

class TaskScheduler:
    def __init__(self):
        self.queue = deque()
    
    def add_task(self, task):
        self.queue.append(task)
    
    def process_task(self):
        if self.queue:
            task = self.queue.popleft()
            print(f"Processing task: {task}")
        else:
            print("No tasks to process")

# Example usage
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")

scheduler.process_task()  
scheduler.process_task()  
scheduler.process_task()  
scheduler.process_task()  # Should print "No tasks to process"


