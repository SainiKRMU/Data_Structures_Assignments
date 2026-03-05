
# Algorithmic Efficiency & Recursion Toolkit (AERT)
# Unit 1 - Data Structures Assignment

#------------------------------------------------------------------------------------------------------
# Course            : Data Structures
# Name              : Disha Saini
# Roll no.          : 2501730318
# Computer Science Engineering (AI & ML)
# Section           : A
# Submission Date   : 5 March 2026
#____________________________________________________________________________________________________


class StackADT:
    
    def __init__(self):
        # Internal storage using Python list
        self.items = []
    
    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    

# -------------------------------
# Recursive Factorial
# -------------------------------

def factorial(n):
    if n < 0:
        return "Invalid input (n must be >= 0)"
    
    if n == 0 or n == 1:   # Base case
        return 1
    
    else:
        return n * factorial(n - 1)


# -------------------------------
# Naive Recursive Fibonacci
# -------------------------------

fib_naive_calls = 0
def fib_naive(n):
    global fib_naive_calls
    fib_naive_calls += 1
    
    if n <= 1:   # Base case
        return n
    
    else:
        return fib_naive(n - 1) + fib_naive(n - 2)

# -------------------------------
# Memoized Recursive Fibonacci
# -------------------------------

fib_memo_calls = 0
memo = {}

def fib_memo(n):
    global fib_memo_calls
    fib_memo_calls += 1
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        memo[n] = n
        return n
    
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

# -------------------------------
# Tower of Hanoi
# -------------------------------

def hanoi(n, source, auxiliary, destination):
    if n == 1:   # Base case
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Move n-1 from source to auxiliary
    hanoi(n - 1, source, destination, auxiliary)
    
    # Move nth disk
    print(f"Move disk {n} from {source} to {destination}")
    
    # Move n-1 from auxiliary to destination
    hanoi(n - 1, auxiliary, source, destination)

    
# -------------------------------
# Tower of Hanoi using StackADT
# -------------------------------

def hanoi_with_stack(n, source, auxiliary, destination, stack):
    
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        stack.push(move)
        return
    
    hanoi_with_stack(n - 1, source, destination, auxiliary, stack)
    
    move = f"Move disk {n} from {source} to {destination}"
    stack.push(move)
    
    hanoi_with_stack(n - 1, auxiliary, source, destination, stack)


# -------------------------------
# Recursive Binary Search
# -------------------------------

def binary_search(arr, key, low, high):
    
    if low > high:   # Base case (not found)
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == key:
        return mid
    
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    
    else:
        return binary_search(arr, key, mid + 1, high)


# ---------------------------------------------------------------------
# Testing all the programs with examples
# ---------------------------------------------------------------------


# -------------------------------
# Testing StackADT
# -------------------------------

print("\nTesting StackADT")
print("-" * 30)

stack = StackADT()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())
print("Stack size:", stack.size())
print("Popped element:", stack.pop())
print("Stack size after pop:", stack.size())
print("Is stack empty?", stack.is_empty())


# -------------------------------
# Testing Recursive Factorial
# -------------------------------

print("\nTesting Recursive Factorial")
print("-" * 30)

test_values = [0, 1, 5, 10]

for value in test_values:
    print(f"{value}! =", factorial(value))


# -------------------------------
# Testing Naive Fibonacci
# -------------------------------

print("\nTesting Naive Fibonacci")
print("-" * 30)

test_values = [5, 10, 20, 30]

for value in test_values:
    fib_naive_calls = 0   # reset counter
    result = fib_naive(value)
    print(f"Fibonacci({value}) = {result}")
    print("Number of recursive calls:", fib_naive_calls)
    print()
    

# -------------------------------
#Testing Memoized Fibonacci
# -------------------------------

print("\nTesting Memoized Fibonacci")
print("-" * 30)

test_values = [5, 10, 20, 30]

for value in test_values:
    fib_memo_calls = 0
    memo = {}   # reset memo each time
    result = fib_memo(value)
    print(f"Fibonacci({value}) = {result}")
    print("Number of recursive calls:", fib_memo_calls)
    print()


# -------------------------------
# Testing Tower of Hanoi
# -------------------------------

print("\nTesting Tower of Hanoi (N = 3)")
print("-" * 30)

hanoi(3, 'A', 'B', 'C')

print("\nTesting Tower of Hanoi Using Stack (N = 3)")
print("-" * 30)

hanoi_stack = StackADT()

hanoi_with_stack(3, 'A', 'B', 'C', hanoi_stack)

# Since stack reverses order, we pop and store temporarily
temp_list = []

while not hanoi_stack.is_empty():
    temp_list.append(hanoi_stack.pop())

# Reverse to print in correct order
for move in reversed(temp_list):
    print(move)


# -------------------------------
#Testing Recursive Binary Search
# -------------------------------

print("\nTesting Recursive Binary Search")
print("-" * 30)

arr = [1, 3, 5, 7, 9, 11, 13]

test_keys = [7, 1, 13, 2]

for key in test_keys:
    index = binary_search(arr, key, 0, len(arr) - 1)
    print(f"Search {key} -> Index:", index)

# Test empty list
empty_arr = []
print("Search in empty list ->", binary_search(empty_arr, 5, 0, len(empty_arr) - 1))

