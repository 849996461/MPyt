import collections

'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
'''


class Solusion:

    def spiralOrder1(self, matrix: [[int]]) -> [int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res

    def spiralOrder2(self, matrix: [[int]]) -> [int]:
        res = []
        while matrix:
            try:
                res += matrix.pop(0)
                res += [i.pop() for i in matrix]
                res += matrix.pop()[::-1]
                res += [i.pop(0) for i in matrix][::-1]
            except:
                return res
        return res

    def spiralOrder(self, matrix: [[int]]) -> [int]:
        m = len(matrix)
        n = len(matrix[0])
        set = [[False] * n for _ in range(m)]
        ai = [0, 1, 0, -1]
        aj = [1, 0, -1, 0]
        i, j, d = 0, 0, 0
        res = []
        for _ in range(m * n):
            res.append(matrix[i][j])
            set[i][j] = True
            if 0 <= i + ai[d] < m and 0 <= j + aj[d] < n and not set[i + ai[d]][j + aj[d]]:
                pass
            else:
                d = (d + 1) % 4
            i, j = i + ai[d], j + aj[d]

        return res


if __name__ == '__main__':
    print(Solusion().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
