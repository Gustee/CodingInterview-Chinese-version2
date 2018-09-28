# 链表中倒数第k个节点
# 输入一个链表，输出该链表中倒数第k个节点。
# 为了符合大多少人的习惯，本题从1开始计数，即链表的尾节点是到手第1个节点。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        if not head or k <= 0:
            return None
        ahead = head
        for i in range(k-1):
            if ahead.next:
                ahead = ahead.next
            else:
                return None
        behind = head
        while(ahead.next):
            ahead = ahead.next
            behind = behind.next
        return behind

