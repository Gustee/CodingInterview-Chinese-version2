# 找出数组中重复的数字
# 在一个长度为n的数组李的所有数字都在0~n-1的范围内。
# 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次
# 例：输入长度为7的数组[2,3,1,0,2,5,3] 对应的输出是重复的数字2或3

'''
思路：
由于数组中数字的范围都在0~n-1，如果数组中没有重复的数字，那么数组排序之后数字i的数组下标也为i，
存在重复数字，则有些位置可能存在多个数字，有些位置没有数字
从头到尾依次扫描数组中的每个数字。当扫描到下标为i的数字时，首先比较这个数字m是不是等于i。
如果是，则继续扫描下一个数字；
如果不是，则再拿它和第m个数字进行比较，如果它和第m个数字相等就找到了一个重复的数字
如果它和第m个数字不相等，则把第i个数和第m个数交换，直到把m放到下标为m的位置
'''


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if not numbers:
            return False
        for i in numbers:
            if i < 0 or i > len(numbers) - 1:
                return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                m = numbers[i]
                numbers[i] = numbers[m]
                numbers[m] = m
        return False


