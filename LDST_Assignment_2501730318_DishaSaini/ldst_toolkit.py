#Unit-2 Assignment: Linear Data Structures

#------------------------------------------------------------------------------------------------------
# Course            : Data Structures
# Assignment Title  : Linear Data Structures
# Name              : Disha Saini
# Roll no.          : 2501730318
# Computer Science Engineering (AI & ML)
# Section           : A
# Submission Date   : 20 April 2026
#____________________________________________________________________________________________________



# ----------------------------------------------------------------------------------
# Dynamic Array
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.arr = [None] * self.capacity

    def resize(self):
        print("Resizing from", self.capacity, "to", self.capacity * 2)
        new_arr = [None] * (self.capacity * 2)

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity *= 2

    def append(self, x):
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = x
        self.size += 1

    def pop(self):
        if self.size == 0:
            print("Array empty")
            return

        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def display(self):
        print(self.arr[:self.size])


# ----------------------------------------------------------------------------------
# Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, x):
        new_node = Node(x)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete(self, x):
        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if not temp:
            print("Value not found")
            return

        prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ----------------------------------------------------------------------------------
# Doubly Linked List
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new_node = DNode(x)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_after(self, target, x):
        temp = self.head

        while temp:
            if temp.data == target:
                new_node = DNode(x)

                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                return

            temp = temp.next

        print("Target not found")

    def delete_pos(self, pos):
        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for _ in range(pos):
            temp = temp.next
            if not temp:
                return

        if temp.prev:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# ----------------------------------------------------------------------------------
# Stack
class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            return "Empty"

        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if not self.head:
            return None
        return self.head.data


# ----------------------------------------------------------------------------------
# Queue
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)

        if not self.tail:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return "Empty"

        val = self.head.data
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return val

    def front(self):
        if not self.head:
            return None
        return self.head.data


# ----------------------------------------------------------------------------------
# Balanced Paranthesis
def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)

        elif ch in ")}]":
            if stack.peek() == pairs[ch]:
                stack.pop()
            else:
                return False

    return stack.head is None


# ----------------------------------------------------------------------------------
# Main Tests
print("\n--- Dynamic Array Test ---")
da = DynamicArray()
for i in range(12):
    da.append(i)
da.display()

print("Pop:", da.pop())
print("Pop:", da.pop())
print("Pop:", da.pop())
da.display()


print("\n--- Singly Linked List Test ---")
sll = SinglyLinkedList()
sll.insert_beginning(10)
sll.insert_beginning(20)
sll.insert_beginning(30)
sll.insert_end(40)
sll.insert_end(50)
sll.insert_end(60)
sll.traverse()
sll.delete(40)
sll.traverse()


print("\n--- Doubly Linked List Test ---")
dll = DoublyLinkedList()
dll.insert_end(1)
dll.insert_end(2)
dll.insert_end(3)
dll.insert_after(2, 99)
dll.traverse()
dll.delete_pos(1)
dll.traverse()


print("\n--- Stack Test ---")
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Pop:", stack.pop())
print("Peek:", stack.peek())


print("\n--- Queue Test ---")
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Dequeue:", queue.dequeue())
print("Front:", queue.front())


print("\n--- Parentheses Test ---")
print("([]):", is_balanced("([])"))
print("([)]:", is_balanced("([)]"))
print("(((:", is_balanced("((("))
print("Empty:", is_balanced(""))