# 机器人的运动范围
# 地上有一个m行n列的方格。一个机器人从坐标(0,0)的格子开始移动，
# 它每次可以向左右上下移动一格，但不能进入行坐标和列坐标的位数之和大于k的格子。
# 例如，当k=18时，机器人能够进入方格(35,37),因为3+5+3+7=18。
# 问机器人能够到达多少个格子。

class Solution:
    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        visited = [False] * rows * cols
        count = self.movingCountCore(threshold, rows, 0, cols, 0, visited)
        return count

    def movingCountCore(self, threshold, rows, row, cols, col, visited):
        count = 0
        if self.check(threshold, rows, row, cols, col, visited):
            visited[row * cols + col] = True
            count = 1 + self.movingCountCore(threshold, rows, row + 1, cols, col, visited) \
                    + self.movingCountCore(threshold, rows, row - 1, cols, col, visited) \
                    + self.movingCountCore(threshold, rows, row, cols, col + 1, visited) \
                    + self.movingCountCore(threshold, rows, row, cols, col - 1, visited)

        return count

    # 计算一个数的各个位数之和
    def getDigitSum(self, num):
        sum = 0
        while num > 0:
            sum += int(num % 10)
            num = int(num / 10)
        return sum

    # 判断该坐标能否进入
    def check(self, threshold, rows, row, cols, col, visited):
        if 0 <= row < rows and 0 <= col < cols and visited[row * cols + col] == False and self.getDigitSum(
                row) + self.getDigitSum(col) <= threshold:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.getDigitSum(103))
