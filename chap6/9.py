# 和为s的数字
# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。

'''
思路：
定义两个指针，第一个指针指向数组的第一个值，第二个指针指向数组的最后一个值。
如果两个指针指向的数的和等于s，则返回
如果大于s，则左边的指针向右边移动
如果小于s，则右边的指针向左移动
'''


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []
        left = 0
        right = len(array) - 1
        while left < right:
            curSum = array[left] + array[right]
            if curSum == tsum:
                return [array[left], array[right]]
            elif curSum > tsum:
                right -= 1
            else:
                left += 1
        return []