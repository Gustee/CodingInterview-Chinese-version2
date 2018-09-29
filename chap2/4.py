# 在一个二维数组中，每一个都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 完成一个函数输入一个这样的数组和一个整数，判断数组中是否含有该整数

'''
思路：
因为数组中元素大小的排列方式，从数组的右上角开始查找
若比目标元素大，则向下查找
若比目标元素小，则向左查找
'''


class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array or not array[0]:
            return False
        i = 0
        j = len(array[0]) - 1
        while(i < len(array) and j >= 0):
            if(target == array[i][j]):
                return True
            elif(target > array[i][j]):
                i += 1
            else:
                j -=1
        return False