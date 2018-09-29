# 请实现一个函数，把字符串中的每个空格替换成"%20".
# 例如，输入"we are happy." 则输出"we%20are%20happy"


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return s.replace(' ', '%20')