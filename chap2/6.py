# 输入一个链表的头节点，从尾到头反过来打印出每个节点的值
# 链表节点的定义：


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 使用栈
    def printListFromTailToHead_1(self, listNode):
        result = []
        if (listNode == None):
            return result
        while(listNode != None):
            result.append(listNode.val)
            listNode = listNode.next
        result.reverse()
        return result

    # 递归版本
    def printListFromTailToHead_2(self, listNode):
        result = []
        if listNode is None:
            return result
        return self.printListFromTailToHead_2(listNode.next) + [listNode.val]
