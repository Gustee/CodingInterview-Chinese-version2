# 求1+2+...+n
# 求1+2+...+n, 要求不能使用乘除法，for while if else等关键字

'''
思路：
短路求值
python中逻辑运算符的用法，a  and  b，a为False，返回a，a为True，就返回b
'''

class Solution:
    def Sum_Solution(self, n):
        res = n
        temp = res and self.Sum_Solution(n-1)
        res = res+temp
        return res