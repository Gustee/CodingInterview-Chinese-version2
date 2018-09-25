# 二叉搜索树的第k大节点
# 给定一棵二叉搜索树，请找出其中第k大的节点。

'''
思路：
如果按照中序遍历的顺序遍历一棵二叉搜索树，则遍历序列的数值是递增排序的，
所以只需要用中序遍历算法遍历一棵二叉搜索树，我们就可以找出它的第k大节点
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot or k <= 0:
            return None
        self.res = None
        self.k = k
        self.KthNodeCore(pRoot)
        return self.res

    def KthNodeCore(self, pRoot):
        if pRoot.left:
            self.res = self.KthNodeCore(pRoot.left)
        if not self.res:
            if self.k == 1:
                self.res = pRoot
            self.k -= 1
        if not self.res and pRoot.right:
            self.res = self.KthNodeCore(pRoot.right)
        return self.res
