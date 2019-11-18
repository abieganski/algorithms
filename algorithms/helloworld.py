import sys
print(sys.version)

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



tree = None
nodes = list(map(int, input().split()))
for element in nodes:
    tree = insertNode(tree, element)


def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root




from collections import deque



def levelOrderTraversal(root):
    q = deque()
    q.append(root)
    while q:
        curr = q.popleft()
        print(curr.data, end=' ')
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)



