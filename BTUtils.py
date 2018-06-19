from collections import deque

class BinaryTreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self, value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

#traversal
def preOrder(root):
    if root:
        print(root.value)
        preOrder(root.left)
        preOrder(root.right)
        return

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.value)
        return

def levelorder(root):
    dq = deque([])
    dq.append(root)
    while(dq):
        ele = dq.popleft()
        print(ele.value)
        if ele.left:
            dq.append(ele.left)
        if ele.right:
            dq.append(ele.right)

def levelorderReverse(root):
    dq = deque([])
    stack = []
    dq.append(root)
    while(dq):
        ele = dq.popleft()
        if ele.right:
            dq.append(ele.right)
        if ele.left:
            dq.append(ele.left)
        stack.append(ele.value)
    stack.reverse()
    print(*stack, sep=' ')

#max element
##recursive
def maxElement(root):
    max = float('-inf')
    if root:
        left = maxElement(root.left)
        right = maxElement(root.right)
        if left>right:
            max = left
        else:
            max = right
        if root.value > max:
            max = root.value
    return max

##iterative
def maxElementIter(root):
    max = root
    dq = deque([])
    dq.append(root)
    while(dq):
        ele = dq.popleft()
        if ele.value > max.value:
            max = ele
        if ele.left:
            dq.append(ele.left)
        if ele.right:
            dq.append(ele.right)
    print(max.value)

#search element
##recursive
def search(root, x):
    if root:
        if root.value == x:
            return True
        else:
            left = search(root.left, x)
            right = search(root.right, x)
            return left or right
    else:
        return False

##iterative
def searchIter(root, x):
    dq = deque([])
    dq.append(root)
    while(dq):
        ele = dq.pop()
        if ele.value == x:
            return True
        if ele.left:
            dq.append(ele.left)
        if ele.right:
            dq.append(ele.right)
    return False
    
#height
#recursive
def treeHeight(root):
    if not root:
        return 0
    if root:
        left = treeHeight(root.left)
        right = treeHeight(root.right)
        max = left if left > right else right
        return max + 1

##iterative
def treeHeightIter(root):
    dq = deque([])
    level = 0
    dq.append(root)
    dq.append(None)
    while(dq):
        ele = dq.popleft()
        if ele is None:
            if dq:
                dq.append(None)
            level+=1
        else:
            if ele.left:
                dq.append(ele.left)
            if ele.right:
                dq.append(ele.right)
    return level

#half nodes
def halfNodes(root):
    half=0
    dq = deque([])
    dq.append(root)
    while(dq):
        ele = dq.popleft()
        if (ele.left and not ele.right) or (ele.right and not ele.left):
            half+=1
        if ele.left:
            dq.append(ele.left)
        if ele.right:
            dq.append(ele.right)
    return half

#structurally identical trees (data may be different)
def areIdenticalTrees(root1, root2):
    if (root1 and root2):
        return areIdenticalTrees(root1.left, root2.left) and areIdenticalTrees(root1.right, root2.right)
    elif not (root1 or root2):
        return True
    else:
        return False
