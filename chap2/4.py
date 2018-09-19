# 在一个二维数组中，每一个都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 完成一个函数输入一个这样的数组和一个整数，判断数组中是否含有该整数


def find(arr, x):
    if arr is None or len(arr) == 0 or len(arr[0] == 0):
        return False
    found = False
    row = 0
    column = arr[0] - 1
    while row < len(arr) and column >=0:
        if arr[row][column] == x:
            found = True
            break
        elif arr[row][column] > x:
            column -= 1
        elif arr[row][column] < x:
            row += 1
    return found
