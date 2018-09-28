# 构建乘积数组
# 给定一个数组A[0,1,...,n-1]，请构建一个数组B[0,1,...,n-1]
# 其中B中的元素B[i] = A[0]xA[1]x...xA[i-1]xA[i+1]x...xA[n-1], 不能使用除法

class Solution:
    def multiply(self, A):
        if not A:
            return None
        n = len(A)
        B = [1]*n
        for i in range(1, n):
            B[i] = B[i-1] * A[i-1]
        temp = 1
        for i in range(n-2, -1, -1):
            temp *= A[i+1]
            B[i] *= temp
        return B