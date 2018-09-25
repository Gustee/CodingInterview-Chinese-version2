# 和为s的连续正数序列
# 输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）
# 例如：输入15，由于1+2+3+4+5 = 4+5+6 = 7+8 = 15 所以打印出3个连续序列1~5、4~6、7~8

'''
思路：
使用两个数small和big分别表示序列的最小值和最大值。首先把small初始化为1，big初始化为2。
如果从small到big的序列的和大于s，则可以从序列中去掉最小的值，也就是增大small的值
如果从small到big的序列的和小于s，则可以增大big
因为序列中最小需要两个值，所有直到small到(1+s)/2为止
'''


class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        res = []
        small = 1
        big = 2
        mid = (1 + tsum) // 2
        curSum = small + big
        while small < mid:
            if curSum == tsum:
                res.append(range(small, big+1))
            while curSum > tsum and small < mid:
                curSum -= small
                small += 1
                if curSum == tsum:
                    res.append(range(small, big+1))
            big += 1
            curSum += big
        return res
