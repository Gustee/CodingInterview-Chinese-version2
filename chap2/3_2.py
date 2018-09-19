# 不修改数组找出重复的数字
# 在一个长度为n+1的数组里的所有数字都在1~n+1的范围内，所以数组中至少有一个数字是重复的。
# 找出数组中任意一个重复的数字， 但不能修改输入的数组

# 我们把从1-n的数字从中间的数字m分为两部分，前面一半为1~m,后面一半为m+1~n。如果1~m区间的数字的数目超过m，那么这一半的区间里一定包含重复的数字；
# 否则，另一半m+1~n的区间里一定包含重复的数字。那么可以继续把包含重复数字的区间二分，直到找到重复数字。
# 例：假设数组长度为10，若1~5之间的数的数目小于等于5时，那么重复数字一定在6~9之前


def duplicate(arr):
    if arr is None or len(arr) == 0:
        return False

    start = 1
    end = len(arr) - 1
    while end >= start:
        mid = int((end - start) / 2) + start
        count = count_range(arr, start, mid)
        if end == start:
            if count > 1:
                return start
            else:
                break
        if count > (mid - start + 1):
            end = mid
        else:
            start = mid + 1


def count_range(arr, low, up):
    if arr is None or len(arr) == 0:
        return 0
    count = 0
    for i in arr:
        if low <= i <= up:
            count += 1
    return count

