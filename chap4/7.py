# 分行从上到下打印二叉树
# 使用两个指针last和nlast。last始终指向二叉树每一层最右边的节点，nlast指向当前新加入的节点。
# 当last和当前取出的节点相同时，则需要换行，同时last更新为最新加入的节点nlast，即下一行最右的节点。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        t = []
        q = []
        q.append(pRoot)
        last = pRoot
        nlast = None
        while len(q) > 0:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
                nlast = node.left
            if node.right:
                q.append(node.right)
                nlast = node.right
            t.append(node.val)
            if node == last:
                res.append(t)
                t = []
                last = nlast

        return res

