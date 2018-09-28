# 翻转单词顺序
# 输入一个英文句子，翻转句子中单词的顺序，单单词内字符的顺序不变
# 为简单起见，标点符号和普通字母一样处理。

'''
思路：
第一步翻转句子中所有的字符。比如翻转'I am a student'中所有的字符得到'tneduts a ma I'
然后再翻转每个单词中字符的顺序，就得到了'student a am I'
'''

class Solution:
    def ReverseSentence(self, s):
        if not s:
            return ''
        l = len(s)
        s = self.Reverse(s, 0, l-1)
        start = end = 0
        while end <= l:
            if end == l or s[end] == ' ':
                s = self.Reverse(s, start, end-1)
                end += 1
                start = end
            elif s[start] == ' ':
                start += 1
                end += 1
            else:
                end += 1
        return s


    def Reverse(self, s, start, end):
        s = list(s)
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(s)