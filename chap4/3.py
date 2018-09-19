# 顺时针打印矩阵
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        row1 = 0
        col1 = 0
        row2 = len(matrix) - 1
        col2 = len(matrix[row2]) - 1
        res = []
        while (row1 <= row2 and col1 <= col2):
            self.edge(matrix, row1, col1, row2, col2, res)
            row1 += 1
            row2 -= 1
            col1 += 1
            col2 -= 1
        return res

    def edge(self, mat, row1, col1, row2, col2, res):
        if row1 == row2:
            for i in range(col1, col2+1):
                res.append(mat[row1][i])
        elif col1 == col2:
            for i in range(row1, row2+1):
                res.append(mat[i][col1])
        else:
            i = row1
            j = col1
            while (i == row1 and j < col2):
                res.append(mat[i][j])
                j += 1
            while (j == col2 and i < row2):
                res.append(mat[i][j])
                i += 1
            while (i == row2 and j > col1):
                res.append(mat[i][j])
                j -= 1
            while (j == col1 and i > row1):
                res.append(mat[i][j])
                i -= 1


s = Solution()
mat = [[1]]
l = s.printMatrix(mat)
print(l)