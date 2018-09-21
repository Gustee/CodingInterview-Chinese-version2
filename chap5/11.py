# 丑数
# 把只含因子2,3,5的数称为丑数。
# 按从小到大的第n个丑数, 把1当作第一个丑数

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        uglyNumbers =[0 for i in range(index+1)]
        uglyNumbers[0] = 1
        nextIndex = 1
        m2 = m3 = m5 = 0
        while nextIndex < index:
            curMin = min(uglyNumbers[m2]*2, uglyNumbers[m3]*3, uglyNumbers[m5]*5)
            uglyNumbers[nextIndex] = curMin
            while uglyNumbers[m2]*2 <= curMin:
                m2 += 1
            while uglyNumbers[m3]*3 <= curMin:
                m3 += 1
            while uglyNumbers[m5]*5 <= curMin:
                m5 += 1
            nextIndex += 1
        return uglyNumbers[nextIndex-1]
