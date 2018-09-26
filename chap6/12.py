# 左旋转字符串
# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部
# 实现一个函数实现字符串左旋转操作

'''
思路：
以abcdefg为例，先把字符串分成两部分'ab'和'cdefg'
先分别翻转这两个部分，于是得到'ba'和'gfedc'
最后再翻转整个字符串得到'cdefgab'即我们需要的字符串
'''

class Solution:
    def LeftRotateString(self, s, n):
        pass