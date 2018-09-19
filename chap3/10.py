# 反转链表
# 输入一个链表，反转链表后，输出新链表的表头。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        preNode = pHead
        curNode = pHead.next
        if not curNode.next:
            curNode.next = pHead
            pHead.next = None
            return curNode
        nextNode = curNode.next
        preNode.next = None
        while nextNode :
            curNode.next = preNode
            preNode = curNode
            curNode = nextNode
            nextNode = nextNode.next
        curNode.next = preNode
        return curNode



