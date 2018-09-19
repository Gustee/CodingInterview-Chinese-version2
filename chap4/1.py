# 二叉树的镜像
# 输入一课二叉树，该函数输出它的镜像

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return
        if not root.left and not root.right:
            return
        t = root.left
        root.left = root.right
        root.right = t
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)