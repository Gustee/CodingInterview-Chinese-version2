# 给你一根长度为n的绳子，请把绳子剪成m段，每段绳子的长度记为k[0],k[1],...k[m]，请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？
import random


class Solution:

    def maxProductAfterCutting_dp(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

        products = [0, 1, 2, 3]

        for i in range(4, length + 1):
            m = 0
            for j in range(1, int(i / 2) + 1):
                current = products[j] * products[i - j]
                m = max(m, current)
            products.append(m)

        return products[length]

    def maxProductAfterCutting_greedy(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

        # 尽可能多地剪去长度为3的绳子段
        timesOf3 = int(length / 3)

        # 当绳子最后剩下的长度为4时，不能再剪去长度为3的绳子段
        # 则把绳子剪成长度为2的两段
        if length - timesOf3 * 3 == 1:
            timesOf3 -= 1
        timesOf2 = int((length - timesOf3 * 3) / 2)

        return pow(3, timesOf3) * pow(2, timesOf2)


if __name__ == '__main__':
    s = Solution()
    for i in range(100):
        x = random.randint(1, 1000)
        if s.maxProductAfterCutting_dp(x) != s.maxProductAfterCutting_greedy(x):
            print('fuck')
            break
    print('yes')
