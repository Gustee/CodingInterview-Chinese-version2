# 重建二叉树
# 输入某个二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
# 例如输入前序遍历序列[1,2,4,7,3,5,6,8]和中序遍历序列[4,7,2,1,5,3,8,6],
# 则重建如下图所示二叉树
#      1
#   2     3
# 4     5   6
#   7      8

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left = None


def construct(preorder, inorder):
    if preorder is None or len(preorder) == 0:
        return None
    if inorder is None or len(inorder) == 0:
        return None
    val = preorder[0]
    head = TreeNode(val)
    index = inorder.index(val)
    head.left = construct(preorder[1:1+index], inorder[0:index])
    head.right = construct(preorder[1+index:], inorder[index+1:])
    return head




