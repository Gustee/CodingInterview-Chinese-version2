# 数组中出现次数超过一半的数字
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count = 1
        num = numbers[0]
        for i in numbers[1:]:
            if i == num:
                count += 1
            else:
                count -= 1
                if count == 0:
                    num = i
                    count = 1
        sum = 0
        for j in numbers:
            if j == num:
                sum += 1
        if sum > int(len(numbers)/2):
            return num
        return 0

