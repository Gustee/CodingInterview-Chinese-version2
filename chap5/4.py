# 连续子数组的最大和
# 输入一个整型数组，数组里有正数也有负数。
# 数组中的一个或连续多个整数组成一个子数组。
# 求所有子数组的和的最大值。

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        sum = array[0]
        max = array[0]
        for i in array[1:]:
            # 如果前面的元素和小于0，那么放弃之前的累加，sum从当前元素开始。
            if sum <= 0:
                sum = i
            else:
                sum += i
            if sum > max:
                max = sum
        return max


l = [1, -2, 3, 10, -4, 7, 2, -5]
s = Solution()
s.FindGreatestSumOfSubArray(l)