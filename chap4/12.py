# 二叉搜索树与双向链表
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的节点，只能调整树中节点指针的指向。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None

        lastNode = self.ConvertCore(pRootOfTree, None)
        head = lastNode
        while head and head.left:
            head = head.left
        return head

    def ConvertCore(self, node, lastNode):
        if node == None:
            return None
        curNode = node
        if curNode.left:
            lastNode = self.ConvertCore(curNode.left, lastNode)
        curNode.left = lastNode
        if lastNode:
            lastNode.right = curNode
        lastNode = curNode
        if curNode.right:
            lastNode = self.ConvertCore(curNode.right, lastNode)
        return lastNode

