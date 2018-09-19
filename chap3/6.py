# 表示数值的字符串
# 请实现一个函数用来判断字符串是否表示数值。
# 例如'+100'，'5e2', '-1E-16'都表示数值，'12e','+-5','1.2.3'都不是

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s or len(s) == 0:
            return False
        l = [i.lower() for i in s]
        if 'e' in l:
            i = l.index('e')
            front = l[:i]
            behind = l[i+1:]
            if '.' in behind or len(behind) == 0:
                return False
            return self.isNum(front) and self.isNum(behind)
        else:
            return self.isNum(l)

    def isNum(self, l):
        num = '1234567890.-+'
        dotCount = 0
        for i in range(len(l)):
            if l[i] =='.':
                dotCount += 1
            if l[i] not in num:
                return False
            else:
                if l[i] in '+-' and i != 0:
                    return False
        if dotCount > 1:
            return False
        return True
