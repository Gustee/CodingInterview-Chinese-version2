# 求斐波拉契数列的第n项

# 递归
def Fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)

# 非递归
def Fibonacci_(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    res = 0
    for i in range(2,n+1):
        res = a + b
        a = b
        b = res
    return res

