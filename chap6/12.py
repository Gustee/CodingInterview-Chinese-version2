# 左旋转字符串
# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部
# 实现一个函数实现字符串左旋转操作

'''
思路：
以abcdefg, n=2为例，先把字符串分成两部分'ab'和'cdefg'
先分别翻转这两个部分，于是得到'ba'和'gfedc'
最后再翻转整个字符串得到'cdefgab'即我们需要的字符串
'''

class Solution:
    def LeftRotateString(self, s, n):
        if not s:
            return ''
        l = len(s)
        left = s[0: n]
        right = s[n: l]
        left = self.Reverse(left, 0, n-1)
        right = self.Reverse(right, 0, len(right)-1)
        s = left + right
        print(s)
        return self.Reverse(s, 0, l-1)


    def Reverse(self, s, start, end):
        s = list(s)
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(s)
