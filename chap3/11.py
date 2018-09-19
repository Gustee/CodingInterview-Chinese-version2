# 合并两个排序的链表
# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        newList = ListNode(0)
        node = newList
        while pHead1 or pHead2:

            while pHead1 and pHead2:
                if pHead1.val < pHead2.val:
                    node.next = pHead1
                    node = node.next
                    pHead1 = pHead1.next
                else:
                    node.next = pHead2
                    node = node.next
                    pHead2 = pHead2.next
            while pHead1 and not pHead2:
                node.next = pHead1
                node = node.next
                pHead1 = pHead1.next
            while pHead2 and not pHead1:
                node.next = pHead2
                node = node.next
                pHead2 = pHead2.next
        return newList.next

