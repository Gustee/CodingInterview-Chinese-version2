# 二叉搜索树的后序遍历序列
# 输入一个整数数组，判断该数组是不是某个二叉搜索树的后序遍历结果。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def SquenceOfBST(self, sequence):
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        index = self.find(sequence[:len(sequence)-1], root)
        return self.SquenceOfBST(sequence[:index]) and self.SquenceOfBST(sequence[index:len(sequence)-1])


    def find(self, sequence, num):
        global i
        for i in range(len(sequence)):
            if sequence[i] > num:
                return i
        return i


