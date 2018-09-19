# 找出数组中重复的数字
# 在一个长度为n的数组李的所有数字都在0~n-1的范围内。
# 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次
# 例：输入长度为7的数组[2,3,1,0,2,5,3] 对应的输出是重复的数字2或3


def duplicate(arr):
    if arr is None or len(arr) == 0:
        return False
    for i in arr:
        if i < 0 or i > len(arr) - 1:
            return False
    for i in range(len(arr)):
        while arr[i] != i:
            if arr[i] == arr[arr[i]]:
                return arr[i]
            else:
                t = arr[i]
                arr[i] = arr[arr[i]]
                arr[t] = t

    return False
