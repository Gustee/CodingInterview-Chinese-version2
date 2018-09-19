# 删除链表的节点
# 给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。
class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class Solution:
    def DeleteNode(self, head, node):
        if not head or not node:
            return

        # 链表只有一个节点，删除该节点
        if node is head:
            head = None
        # 要删除的节点不是尾节点
        if node.next is not None:
            t = node.next
            node.value = t.value
            node.next = t.next
        # 要删除的节点是尾节点
        if node.next is None:
            c = head
            while c.next.next is not None:
                c = c.next
            c.next = None





a = ListNode('a')
b = ListNode('b')
c = ListNode('c')
a.next = b
b.next = c
d = ListNode('d')
e = ListNode('e')
c.next = d
d.next = e

s = Solution()
s.DeleteNode(a, e)
s.DeleteNode(a, d)
head = a
while head is not None:
    print(head.value)
    head = head.next


