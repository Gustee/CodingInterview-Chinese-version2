# 从上到下打印二叉树
# 不分行从上到下打印二叉树。

'''
思路：
二叉树的层次遍历
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        q = []
        res = []
        q.append(root)
        while len(q) > 0:
            node = q.pop(0)
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res