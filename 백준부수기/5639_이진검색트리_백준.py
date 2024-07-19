import sys

sys.setrecursionlimit(10000)

class Node:
    def __init__(self, value:int = None, parents_value = None, left:'Node' = None, right:'Node' = None):
        self.value = value
        self.left = left
        self.right = right
        self.parents_value = parents_value
    
    def add_left(self, value:int):
        self.left = Node(value, self.value)
    
    def add_right(self, value:int):
        self.right = Node(value, self.parents_value)

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.value)

    def preorder(self):
        print(self.value)
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()

input_list = []
while True:
    try:
        input_value = int(input())
        input_list.append(input_value)
    except:
        break

N = len(input_list)
i = 1

root = Node(input_list[0], float('inf'))

def add(node: Node):
    global i
    if i < N and input_list[i] < node.value:
        node.add_left(input_list[i])
        i += 1
        add(node.left)
    
    if i < N and node.value < input_list[i] < node.parents_value:
        node.add_right(input_list[i])
        i += 1
        add(node.right)

add(root)

root.postorder()