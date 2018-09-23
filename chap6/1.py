# 在排序数组中查找数字
# 统计一个数字在排序数组中出现的次数。
# 例如，输入排序数组[1,2,3,3,3,3,4,5]和数字3，输出4

'''
思路：
假设要统计数字k在排序数组中出现的次数，使用二分查找直接找到第一个k和最后一个k
分析找到第一个k：
如果中间的数字比k大，那么k只有可能出现在数组的前半段，如果中间的数字比k小，k出现在后半段
如果中间的数字等于k，则判断中间数字的前一个数字是不是k，如果不是则刚好是第一个k
如果前一个数字也是k，则需要在数组的前半段继续查找。
找到最后一个k同理
'''

class Solution:
    def GetNumberOfK(self, data, k):
        if data:
            first = self.GetFirstK(data, k)
            last = self.GetLastK(data, k)
            if first >= 0 and last >= 0:
                return last - first + 1
        return 0

    def GetFirstK(self, data, k):
        start = 0
        end = len(data)-1
        while start <= end:
            mid = start + (end - start) // 2
            if data[mid] == k:
                if mid > 0 and data[mid-1] != k or mid == 0:
                    return mid
                else:
                    end = mid - 1
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return -1


    def GetLastK(self, data, k):
        l = len(data)
        start = 0
        end = l - 1
        while start <= end:
            mid = start + (end - start) // 2
            if data[mid] == k:
                if mid < l - 1 and data[mid + 1] != k or mid == l-1:
                    return mid
                else:
                    start = mid + 1
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return -1
