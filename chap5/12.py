# 第一次只出现一次的字符
# 字符串中第一次只出现第一次的字符
# 在字符串中找出第一个只出现第一个只出现一次的字符。

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == None or len(s) <= 0:
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1