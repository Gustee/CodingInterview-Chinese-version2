# 正则表达式匹配
# 实现一个函数用来匹配包含'.'和'*'的正则表达式。
# 模式中的字符'.'表示任意一个字符
# '*'表示它前面的字符可以出现任意次数(含0次）

class Solution:
    def isMatch(self, s, pattern):
        # 若模式串为空时，s同时为空，则返回True
        if pattern == '':
            return s == ''
        # 若模式串长度为1时，判断s长度是否为1，且字符相等，或匹配串为'.'
        if len(pattern) == 1:
            return len(s) == 1 and (pattern[0] == '.' or s[0] == pattern[0])
        if s == pattern:
            return True
        if pattern[1] != '*':
            if s == '':
                return False
            return (s[0] == pattern[0] or pattern[0] == '.') and self.isMatch(s[1:], pattern[1:])
        else:
            while s and (s[0] == pattern[0] or pattern[0] == '.'):
                if self.isMatch(s, pattern[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, pattern[2:])
        # while s and (s[0] == p[0] or p[0] == '.'):
        #     # 到了while循环，说明p[1]为*，所以递归调用匹配s和p[2:](*号之后的匹配规则)
        #     # 用于跳出函数，当s循环到和*不匹配的时候，则开始去匹配p[2:]之后的规则
        #     if self.isMatch(s, p[2:]):
        #         return True
        #     # 当匹配字符串和匹配规则*都能匹配的时候，去掉第一个字符成为新的匹配字符串，循环
        #     s = s[1:]
        # # 假如第一个字符和匹配规则不匹配，则去判断之后的是否匹配
        # return self.isMatch(s, p[2:])


class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    hash = None

    def isMatch(self, s, p):
        if self.hash is None:
            self.hash = {}
        key = s + p
        if key in self.hash:
            return self.hash[key]

        if p == '':
            return s == ''
        if s == '':
            if len(p) % 2 == 1:
                return False
            i = 1
            while i < len(p):
                if p[i] != '*':
                    return False
                i += 2
            return True

        if len(p) > 1 and p[1] == '*':
            if p[0] == '.':
                self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            elif p[0] == s[0]:
                self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                self.hash[key] = self.isMatch(s, p[2:])
        elif p[0] == '.':
            self.hash[key] = self.isMatch(s[1:], p[1:])
        else:
            self.hash[key] = s[0] == p[0] and self.isMatch(s[1:], p[1:])

        return self.hash[key]