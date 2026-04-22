#Unit–4 Assignment: Non-Linear & Advanced Data Structures
#------------------------------------------------------------------------------------------------------
# Course            : Data Structures
# Assignment Title  : Non-Linear & Advanced Data Structures
# Name              : Disha Saini
# Roll no.          : 2501730318
# Computer Science Engineering (AI & ML)
# Section           : A
# Submission Date   : 20 April 2026
#____________________________________________________________________________________________________


# ---------------------------------------------------------------------
# BST Implementation
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
            
        return node

    # Search
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # Inorder
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=" ")
            self._inorder(node.right)

    # Delete
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)

        elif key > node.key:
            node.right = self._delete(node.right, key)

        else:
            # Case 1: No child
            if node.left is None and node.right is None:
                return None

            # Case 2: One child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 3: Two children
            temp = self._min_value(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return node

    def _min_value(self, node):
        while node.left:
            node = node.left
        return node


# ---------------------------------------------------------------------
# Graph Implementation

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def print_graph(self):
        for node in self.graph:
            print(node, "->", self.graph[node])

    # BFS
    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            node = queue.pop(0)

            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbor, _ in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()

    # DFS
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        print(start, end=" ")
        visited.add(start)

        for neighbor, _ in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# ---------------------------------------------------------------------
# Hash Table Implementation
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]

    def display(self):
        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)


# ---------------------------------------------------------------------
# Main Test Runner
if __name__ == "__main__":

    print("=========== BST TEST ===========")

    bst = BST()

    nums = [50, 30, 70, 20, 40, 60, 80]
    for n in nums:
        bst.insert(n)

    print("Initial Inorder:")
    bst.inorder()

    print("Search 20:", bst.search(20))
    print("Search 90:", bst.search(90))

    print("\nDelete leaf node (20):")
    bst.delete(20)
    bst.inorder()

    print("\nInsert 65 and delete 60 (one child case):")
    bst.insert(65)
    bst.delete(60)
    bst.inorder()

    print("\nDelete node with 2 children (30):")
    bst.delete(30)
    bst.inorder()

    print("\n=========== GRAPH TEST ===========")

    g = Graph()

    edges = [
        ('A','B',2), ('A','C',4),
        ('B','D',7), ('B','E',3),
        ('C','E',1), ('C','F',8),
        ('D','F',5),
        ('E','D',2), ('E','F',6)
    ]

    for u, v, w in edges:
        g.add_edge(u, v, w)

    print("Adjacency List:")
    g.print_graph()

    print("\nBFS from A:")
    g.bfs('A')

    print("DFS from A:")
    g.dfs('A')
    print()

    print("\n=========== HASH TABLE TEST ===========")

    ht = HashTable(5)

    keys = [10, 15, 20, 7, 12]
    for k in keys:
        ht.insert(k, f"Value{k}")

    print("Hash Table:")
    ht.display()

    print("\nRetrieve values:")
    print("Get 10:", ht.get(10))
    print("Get 15:", ht.get(15))
    print("Get 7:", ht.get(7))

    print("\nDelete 15 (collision bucket):")
    ht.delete(15)
    ht.display()