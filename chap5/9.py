# 礼物的最大值
# 在一个mxn的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。
# 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格，直到到达棋盘的右下角。
# 给定一个棋盘及其上面的礼物，计算最多能拿到多少价值的礼物

class Solution:
    def GetMaxValue(self, values, rows, cols):
        if not values or rows <= 0 or cols <= 0:
            return 0
        maxValues = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                left = 0
                down = 0
                if i > 0:
                    down = maxValues[i+1][j]
                if j > 0:
                    left = maxValues[i][j+1]
                maxValues[i][j] = max(left, down) + values[i*cols+j]
        return maxValues[rows-1][cols-1]



