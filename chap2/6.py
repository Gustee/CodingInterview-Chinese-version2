# 输入一个链表的头节点，从尾到头反过来打印出每个节点的值
# 链表节点的定义：
# class ListNode:
#     def __init__(self, x):
#         self.val
#         self.next = None
# 递归版本
def printListFromTailToHead(listNode):
    result = []
    if listNode is None:
        return result
    return printListFromTailToHead(listNode.next) + [listNode.val]

def printListFromTailToHead(listNode):
    result = []
    if listNode is None:
        return  result
    while listNode.next is not None:
        result.extend([listNode.val])
        listNode = listNode.next
    result.extend([listNode.val])