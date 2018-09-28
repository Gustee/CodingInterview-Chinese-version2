# 不用加减乘除做加法
# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

'''

'''


class Solution:
    def Add(self, a, b):
        while(b):
           a,b = (a^b) & 0xFFFFFFFF,((a&b)<<1) & 0xFFFFFFFF
        return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)