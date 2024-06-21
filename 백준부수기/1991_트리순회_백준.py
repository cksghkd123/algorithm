n = int(input())

class Node:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right
    
    def preorder(self):
        print(self.root,end="")
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()

    def inorder(self):
        if self.left != None:
            self.left.inorder()
        print(self.root,end="")
        if self.right != None:
            self.right.inorder()

    def postorder(self):
        if self.left != None:
            self.left.postorder()
        if self.right != None:
            self.right.postorder()
        print(self.root,end="")

node_dic = {}

for _ in range(n):
    root, left, right = input().split()
    if root not in node_dic:
        node_dic[root] = Node(root)

    if left not in node_dic and left != '.':
        node_dic[left] = Node(left)
    if right not in node_dic and right != '.':
        node_dic[right] = Node(right)
    
    if left != '.':
        node_dic[root].left = node_dic[left]
    if right != '.':
        node_dic[root].right = node_dic[right]
    
node_dic['A'].preorder()
print()
node_dic['A'].inorder()
print()
node_dic['A'].postorder()

    