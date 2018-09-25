# 平衡二叉树
# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
# 如果某二叉树中任意节点的左、右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            # 返回True是因为这是最后的判断依据，在不断递归中，最后是叶子节点，即终止，如果叶子节点时，依然左右子树之差小于1，那么就是平衡二叉树，返回True
            return True
        depth1 = self.GetDepth(pRoot.left)
        depth2 = self.GetDepth(pRoot.right)
        if abs(depth1 - depth2) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def GetDepth(self, root):
        if not root:
            return 0
        return max(self.GetDepth(root.left), self.GetDepth(root.right)) + 1