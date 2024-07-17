class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key)

root = None
while True:
    try:
        input_value = int(input())
        root = insert(root, input_value)
    except:
        break
    
postorder(root)
