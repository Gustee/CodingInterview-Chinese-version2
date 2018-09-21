# 把数字翻译成字符串
# 给定一个数字，我们按照如下规则把它翻译成字符串：
# 0翻译成'a', 1翻译成'b', ... ,11翻译成'l'， 25翻译成'z'
# 一个数字可能有多个翻译，实现一个函数，计算一个数字有多少种不同的翻译

'''
思路：
首先对应10~25的数字都存在两种翻译方式，当最开始的一个或者两个数字被翻译成一个字符后，我们接着翻译后面剩下的数字
定义f(i)表示从第i位数字开始的不同翻译的数目，
比如数字1228，当i=0时，考虑第一个数字1，当1单独翻译成'a'时，翻译的数量等于后面数字228的翻译数量f(1)，
当数字1和后面的2一起翻译成m时，翻译的数量等于后面数字28的翻译数量f(2)，则有f(0)=f(1)+f(2)。综上
f(i) = f(i+1)+g(i,i+1)Xf(i+2),
当第i位和i+1位的两个数字拼接起来的数字在10~25的范围内时，函数g的值为1，否则为0
'''


class Solution:
    def GetTranslationCount(self, number):
        if number < 0:
            return 0
        s =str(number)
        length = len(s)
        results = [0 for i in range(length)]
        results[length-1] = 1
        for i in range(length-2, -1, -1):
            count = results[i+1]
            d1 = int(s[i]) - 0
            d2 = int(s[i+1]) - 0
            if 10 <= 10*d1+d2 <= 25:
                if i < length-2:
                    count += results[i+2]
                else:
                    count += 1
            results[i] = count

        return results[0]
