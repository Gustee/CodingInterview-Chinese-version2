# 二叉树中和为某一值的路径
# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
# 从树的根节点开始往下一直到叶节点所经过的节点形成一条路径

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []
        self.FindPathCore(root, [], 0, expectNumber, res)
        return res

    def FindPathCore(self, node, path, curSum, expectNumber, res):
        curSum += node.val
        path.append(node)
        # 判断是否是叶节点
        isLeaf = not node.left and not node.left
        # 如果是叶节点并且路径之和相等，则将路径添加到结果数组
        if isLeaf and curSum == expectNumber:
            onepath = []
            for node in path:
                onepath.append(node.val)
            res.append(onepath)
        if node.left:
            self.FindPathCore(node.left, path, curSum, expectNumber, res)
        if node.right:
            self.FindPathCore(node.right, path, curSum, expectNumber, res)
        path.pop()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(7)
n6 = TreeNode(6)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

s = Solution()
res = s.FindPath(n1, 10)
print(res)

