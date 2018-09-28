# 矩阵中的路径
# 设计一个函数用来判断咋在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左右上下移动一格。
# 如果一条路径经过了矩阵中的某一格，那么该路径不能再次进入该格子。


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix or path is None or rows < 0 or cols < 0:
            return False
        # 使用一个数组记录该位置是否已经被访问过
        visited = [False] * rows * cols
        length = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, row, cols, col, path, length, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, row, cols, col, path, length, visited):
        if len(path) == length:
            return True
        flag = False
        index = row * cols + col
        if 0 <= row < rows and 0 <= col < cols and path[length] == matrix[index] and visited[index] == False:
            length += 1
            visited[index] = True
            # 从四个方向递归去寻找下一个字符
            flag = self.hasPathCore(matrix, rows, row + 1, cols, col, path, length, visited) or \
                   self.hasPathCore(matrix, rows, row - 1, cols, col, path, length, visited) or \
                   self.hasPathCore(matrix, rows, row, cols, col + 1, path, length, visited) or \
                   self.hasPathCore(matrix, rows, row, cols, col - 1, path, length, visited)
            # 如果没有找到则回退到上一个字符，并将该位置标记为未访问
            if not flag:
                length -= 1
                visited[index] = False
        return flag

