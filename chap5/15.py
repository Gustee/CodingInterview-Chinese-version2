# 两个链表的第一个公共节点
# 输入两个链表，找出他们的第一个公共节点

'''
思路：
先求出两个链表的长度，然后求两个链表的长度差d,然后较长的链表先走d步，
最后两个指针同步移动，最后两个指针相遇的节点即时两个链表的交点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        l1 = l2 = 0
        head = pHead1
        while head:
            l1 += 1
            head = head.next
        head = pHead2
        while head:
            l2 += 1
            head = head.next
        if l1 >= l2:
            d = l1 - l2
            h1 = pHead1
            h2 = pHead2
            while d > 0:
                h1 = h1.next
                d -= 1
            while h1 != h2:
                h1 = h1.next
                h2 = h2.next
            return h1
        else:
            d = l2 - l1
            h1 = pHead1
            h2 = pHead2
            while d > 0:
                h2 = h2.next
                d -= 1
            while h1 != h2:
                h1 = h1.next
                h2 = h2.next
            return h2