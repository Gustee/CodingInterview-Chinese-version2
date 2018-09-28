# 扑克牌中的顺子
# 从扑克牌中随机抽取5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# 2~10为数字本事，A为1，J为11，Q为12，K为13，大小王为0可以看成任意数字

'''
思路：
首先把数组排序
然后统计数组中0的个数
最后统计排序之后的数组中相邻数字之间的空缺总数
'''

class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numbers.sort()
        numOfZero = 0
        numOfGap = 0
        for i in numbers:
            if i != 0:
                break
            numOfZero += 1
        small = numOfZero
        big = small + 1
        while big < len(numbers):
            if numbers[small] == numbers[big]:
                return False
            numOfGap += (numbers[big] - numbers[small] - 1)
            small += 1
            big += 1
        if numOfZero >= numOfGap:
            return True
        return False
