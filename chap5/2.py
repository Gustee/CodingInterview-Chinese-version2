# 最小的k个数
# 输入n个整数，找出其中最小的k个数。
# 例，输入[4,5,1,6,2,7,3,8],则最小的4个数字是1,2,3,4


'''
思路一：
根据快排的划分过程，如果选中的数刚好是数组的第k个数字，那么比第k个数小的所有数都位于数组的左边，
比第k个数大的所有数字都位于数组的右边，这样调整后，位于数组左边的k个数就是最小的k个数字了。
'''

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput:
            return []
        length = len(tinput)
        if k <= 0 or k > length:
            return []
        start, end = 0, length-1
        index = self.Partition(tinput, start, end)
        while index != k-1:
            if index > k-1:
                end = index - 1
                index = self.Partition(tinput, start, end)
            else:
                start = index + 1
                index = self.Partition(tinput, start, end)
        l = []
        for i in range(k):
            l.append(tinput[i])
        return l

    def Partition(self, l, start, end):
        key = l[end]
        x = start-1
        for i in range(start, len(l)):
            if l[i] < key:
                x += 1
                t = l[i]
                l[i] = l[x]
                l[x] = t
        x = x + 1
        t = l[x]
        l[x] = l[end]
        l[end] = t
        return x


s = Solution()
l = [4,5,1,6,2,7,3,8]
print(s.GetLeastNumbers_Solution(l, 4))
