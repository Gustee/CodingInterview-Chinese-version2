# 字符串的排列
# 输入一个字符串,打印出该字符串中字符的所有排列
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]
        charList = list(ss)
        res = []
        self.PermutationCore(charList, 0, res)
        res.sort()
        return res

    def PermutationCore(self, cs, i, res):
        if i == len(cs) - 1:
            s = ''.join(cs)
            if s not in res:
                res.append(''.join(cs))
            return
        else:
            for j in range(i, len(cs)):
                self.swap(cs, i, j)
                self.PermutationCore(cs, i+1, res)
                self.swap(cs, i, j)

    def swap(self, arr, i, j):
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t

