# 之字形打印二叉树
# 实现一个函数按照之字形顺序打印二叉树，即第一层按照从左到右的顺序打印，
# 第二层按照从右到左的顺序打印，第三层再按照从左到右的顺序打印。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        temp = []
        curStack, nextStack = [pRoot], []
        flag = True
        while curStack or nextStack:
            node = curStack.pop()
            temp.append(node.val)
            if flag:
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            else:
                if node.right:
                    nextStack.append(node.right)
                if node.left:
                    nextStack.append(node.left)
            if not curStack:
                flag = not flag
                res.append(temp)
                temp = []
                curStack = nextStack
                nextStack = []
        return res

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

s = Solution()
res = s.Print(n1)
print(res)
