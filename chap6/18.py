# 股票的最大利润
# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

'''
思路：
股票交易的利润来自股票买入和卖出价格的差价
最大的利润就是数组中所有数对的最大差值
定义函数diff(i)表示当卖出价为数组中第i个数字时可能获得的最大利润。在卖出价固定时，买入价格越低获得的利润越大
如果在扫描到数组中的第i个数字时，只要能够记住之前的i-1个数字中的最小值，就能计算出当前价位卖出时可得到的最大利润
'''


class Solution:
    def MaxDiff(self, numbers):
        if not numbers:
            return 0
        min = numbers[0]
        maxDiff = numbers[1] - min
        for i in range(2, len(numbers)):
            if numbers[i-1] < min:
                min = numbers[i-1]
            curDiff = numbers[i] - min
            if curDiff > maxDiff:
                maxDiff = curDiff
        return maxDiff