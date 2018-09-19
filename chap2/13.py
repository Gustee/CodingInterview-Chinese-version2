# 旋转数组的最小数字
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素


def min(arr):
    start = 0
    end = len(arr)-1
    while end >= start:
        mid = int((end - start) / 2) + start
        if arr[mid] >= arr[start]:
            start = mid+1
        if arr[mid] <= arr[end]:
            end = mid
    return arr[end]


l = [6,8,9,2,4]
print(min(l))