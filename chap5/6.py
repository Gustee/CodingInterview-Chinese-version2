# 数字序列中某一位的数字
# 数字以012345678910112131415...的格式序列化到一个字符序列中。
# 在这个序列中，第5位是5，第13位是1，第19位是4，等等
# 实现一个函数，求任意第n位对应的数字。

class Solution:
    def DigitAtIndex(self, index):
        if index < 0:
            return -1
        digits = 1
        while True:
            num = self.CountOfInt(digits)
            if index < num * digits:
                return self.AtIndex(index, digits)
            index -= digits * num
            digits += 1
        return -1

    # 当确定该位数字位于某个m位数之中后，使用如下函数求出结果
    def AtIndex(self, index, digits):
        startNum = 0
        if digits != 1:
            startNum = pow(10, digits - 1)
        number = startNum + int(index/digits)
        indexFromRight = digits - index % digits
        for i in range(1, indexFromRight):
            number = int(number/10)
        return number % 10

    # 计算m位的数字总共有多少个
    def CountOfInt(self, digits):
        if digits == 1:
            return 10
        count = int(pow(10, digits-1))
        return 9 * count

if __name__ == '__main__':
    s = Solution()
    x = s.DigitAtIndex(1001)
    print(x)