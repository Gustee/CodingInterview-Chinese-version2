# 数组中数值和下标相等的元素
# 假设一个单调递增的数组里的每个元素都是整数并且是唯一的
# 实现一个函数，找出数组中任意一个数值等于其下标的元素
# 例如在数组中[-3,-11,3,5]数字3与其下标相等


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
