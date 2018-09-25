# 数组中数值和下标相等的元素
# 假设一个单调递增的数组里的每个元素都是整数并且是唯一的
# 实现一个函数，找出数组中任意一个数值等于其下标的元素
# 例如在数组中[-3,-11,3,5]数字3与其下标相等

'''
思路：
由于数组是单调递增的，使用二分查找的方法来找该元素。i=m
假设某一步抵达数组中的第i个数字m，如果该数字的值刚好也是i，即i=n，即找到该元素
如果m>i,因为数字是单条递增，那么第i+k个数字的值肯定大于m+k，即i后面所有的数字的值都比下标大，所以下一轮查找，从i的左边中查找
如果m<i,则在i的右边找
'''


class Solution:
    def GetNumberSameAsIndex(self, number):
        if not number:
            return -1
        l = len(number)
        start = 0
        end = l - 1
        while start <= end:
            mid = start + (end - start) // 2
            if number[mid] == mid:
                return mid
            if mid < number[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
