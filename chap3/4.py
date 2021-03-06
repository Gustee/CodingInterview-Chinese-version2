# 删除链表中重复的节点
# 在一个排序的链表中，如何删除重复的节点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication_1(self, pHead):
        if pHead is None:
            return
        res = []
        node = pHead
        while node:
            res.append(node.val)
            node = node.next
        res = list(filter(lambda c: res.count(c) == 1, res))
        newlist = ListNode(0)
        pre = newlist
        for i in res:
            node = ListNode(i)
            pre.next = node
            pre = pre.next
        return newlist.next

    def deleteDuplication_2(self, pHead):
        if pHead is None:
            return
        preNode = None
        node = pHead
        while node:
            nextNode = node.next
            toDelete = False
            if nextNode and nextNode.val == node.val:
                toDelete = True
            if not toDelete:
                preNode = node
                node = node.next
            if toDelete:
                value = node.val
                delNode = node
                while delNode and delNode.val == value:
                    delNode = delNode.next
                if not preNode:
                    pHead = delNode
                    node = delNode
                    continue
                else:
                    preNode.next = delNode
                node = preNode
        return pHead



