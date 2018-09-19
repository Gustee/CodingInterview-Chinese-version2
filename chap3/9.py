# 链表中环的入口节点
# 如果一个链表中包含环，如何找出环的入口节点。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def EntryNodeOfLoop(self, head):
        if (head == None or head.next == None):
            return None
        fast = head
        slow = head
        flag = False
        while (slow != None):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                flag = True
                break
        if (flag):
            fast = head
            while (slow != fast):
                fast = fast.next
                slow = slow.next
            return fast
        else:
            return None