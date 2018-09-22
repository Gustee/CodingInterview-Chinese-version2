# 数组中的逆序对
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组，求出这个数组中的逆序对的总数
# 例如数组[8,5,6,4]一共存在5个逆序对。

'''
思路：
先把数组划分成子数组，统计子数组内部的逆序对的数目，然后在统计出两个相邻子数组之间的逆序对的数目。
统计两个子数组之间的逆序对数目的方法
先用两个指针分别指向两个子数组的末尾，每次比较两个指针指向的数字，
如果第一个子数组中的数字大于第二个子数组中的数字，
则构成逆序对，并且逆序对的数目等于第二个子数组中剩余数字的个数。
如果第一个子数组中的数字小于等于第二个子数组中的数字，则不构成逆序对，
并将较大的数拷贝到辅助数组，同时指针向前移动。
'''

class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        l = len(data)
        copy = [0] * l
        for i in range(l):
            copy[i] = data[i]
        count = self.InversePairsCore(data, copy, 0, l-1)
        return count

    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        mid = start + int((end - start)/2)
        left = self.InversePairsCore(copy, data, start, mid)
        right = self.InversePairsCore(copy, data, mid+1, end)
        # i初始化为前半段最后一个数字的下标
        i = mid
        # j初始化为后半段最后一个数字的下标
        j = end
        # index初始化为辅助数组的最后一个数字的下标
        index = end
        count = 0
        while i >= start and j >= mid+1:
            if data[i] > data[j]:
                copy[index] = data[i]
                i -= 1
                count += j - mid
            else:
                copy[index] = data[j]
                j -= 1
            index -= 1
        while i >= start:
            copy[index] = data[i]
            index -= 1
            i -= 1
        while j >= mid + 1:
            copy[index] = data[j]
            index -= 1
            j -= 1

        return count + left + right
