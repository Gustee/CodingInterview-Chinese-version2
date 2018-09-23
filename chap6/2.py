# 0~n-1中缺失的数字
# 一个长度为n-1的递增排序数组中的所有数字都是惟一的，并且每个数字都在范围0~n-1之内。
# 在范围0~n-1内的n个数字中有且只有一个数字不在该数组中，找出这个数字

'''
思路：
因为这些数字在数组中是排序的，因此数组中开始的一些数字与他们的下标相同。也就是说，0在下标为0的位置，
1在下标为1的位置，如果不在数组中的那个数字记为m，那么所有比m小的数字的下标都与他们的值相同
由于m不在数组中，那么m+1处在下标为m的位置，以此类推。
基于二分查找
如果中间元素的值和下标相同，那么下一轮查找只需要查找右半边；
如果中间元素的值和下标不相等，并且它前面一个元素和它的下标相等，则它的下标就是数组中不存在的数字
如果中间元素的值和下标不相等，并且它前面一个元素和它的下标不相等，则继续在左半边查找。
'''


class Solution:
    def GetMissingNumber(self, numbers):
        if not numbers:
            return -1
        l = len(numbers)
        start = 0
        end = l - 1
        while start <= end:
            mid = start + (end - start) // 2
            if numbers[mid] != mid:
                if mid == 0 or numbers[mid - 1] == mid - 1:
                    return mid
                end = mid - 1
            else:
                start = mid + 1
        if start == l:
            return l
        return -1

if __name__ == '__main__':
    s = Solution()
    l = [0,1,2,3,5,6,7,8]
    print(s.GetMissingNumber(l))