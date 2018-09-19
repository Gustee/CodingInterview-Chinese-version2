# 树的子结构
# 输入两棵二叉树A和B，判断B是不是A的子结构

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1HaveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result


    def DoesTree1HaveTree2(self, a, b):
        if not b:
            return True
        if not a:
            return False
        if a.val != b.val:
            return False
        return self.DoesTree1HaveTree2(a.left, b.left) and self.DoesTree1HaveTree2(a.right, b.right)
