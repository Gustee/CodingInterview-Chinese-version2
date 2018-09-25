# 二叉树的深度
# 输入一棵二叉树的根节点，求该树的深度。
# 从根节点到叶节点依次经过的节点（含根，叶节点）形成树的一条路径，最长路径的长度为树的深度。

'''
思路：
如果一棵树只有一个节点，那么它的深度为1
如果根节点只有左子树而没有右子树，那么树的深度应该是其左子树的深度加1
如果根节点只有右子树没有左子树，同理
如果既有左子树也有右子树，那么树的深度就是左、右子树深度的较大值加1
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left, right) + 1