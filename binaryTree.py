from BTUtils import *

#main
if __name__ == '__main__':
    c4 = BinaryTreeNode(7)
    c3 = BinaryTreeNode(6)
    c2 = BinaryTreeNode(5)    
    c1 = BinaryTreeNode(4)
    b2 = BinaryTreeNode(3, left=c3, right=c4)
    b1 = BinaryTreeNode(2, left=c1, right=c2)
    r1 = BinaryTreeNode(1, left=b1, right=b2)

    q4 = BinaryTreeNode(7)
    q3 = BinaryTreeNode(6)
    q2 = BinaryTreeNode(5)    
    q1 = BinaryTreeNode(4)
    p2 = BinaryTreeNode(3, left=q3, right=q4)
    p1 = BinaryTreeNode(2, left=q1, right=q2)
    r2 = BinaryTreeNode(1, left=p1, right=p2)
    print(width(r1))