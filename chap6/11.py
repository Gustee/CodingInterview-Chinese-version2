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
        # write code here
        if s == None or len(s) <= 0:
            return ''
        s = list(s)
        s = self.Reverse(s)
        pStart = 0
        pEnd = 0
        listTemp = []
        result = ''

        while pEnd < len(s):
            if pEnd == len(s) - 1:
                listTemp.append(self.Reverse(s[pStart:]))
                break
            if s[pStart] == ' ':
                pStart += 1
                pEnd += 1
                listTemp.append(' ')
            elif s[pEnd] == ' ':
                listTemp.append(self.Reverse(s[pStart:pEnd]))
                pStart = pEnd
            else:
                pEnd += 1
        for i in listTemp:
            result += ''.join(i)
        return result

    def Reverse(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s