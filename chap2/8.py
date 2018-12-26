# 二叉树的下一个节点
# 给定一颗二叉树和其中的一个节点，如何找出中序遍历序列的下一个节点。
# 树的节点出了有两个分别指向左、右子节点的指针，还有一个指向父节点的指针


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        if pNode is None:
            return None
        # 若该节点存在右子树，则后继节点为右子树最左端的节点
        if pNode.right is not None:
            return self.get_most_left(pNode.right)

        parent = pNode.next
        while parent is not None and parent.left is not pNode:
            pNode = parent
            parent = parent.next
        return parent

    # 寻找该节点的最左的节点
    def get_most_left(self, node):
        if node is None:
            return node
        while node.left is not None:
            node = node.left
        return node

