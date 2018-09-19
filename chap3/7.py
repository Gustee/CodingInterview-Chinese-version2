# 调整数组顺序使奇数位于偶数前面
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有奇数位于数组的前半部分，所有的偶数位于数组的后半部分

class Solution:
    def reOrderArray_1(self, array):
        # write code here
        if not array or len(array) == 0:
            return
        x = -1
        for i in range(len(array)):
            if array[i] % 2 != 0:
                x += 1
                self.swap(array, i, x)

    def reOrderArray_2(self, array):
        if array is None or len(array) == 0:
            return
        head = 0
        trail = len(array)-1
        while head < trail:
            while array[head] % 2 != 0:
                head += 1
            while array[trail] % 2 == 0:
                trail -= 1
            self.swap(array, head, trail)
            head += 1
            trail -= 1


    def swap(self, arr, i, j):
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t


l = [1,2,3,4,5,6,7]
s = Solution()
s.reOrderArray_2(l)
print(l)