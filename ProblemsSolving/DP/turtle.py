'''
Given: matrix nxm where each (i,j) is integer non-negative number
turtle moves from (0,0) to (n-1, m-1)

Find the maximum sum the turtle can collect on its way
'''


def solution(mat, k_vectors):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            if i == j == 0:
                continue
            max_sum = mat[i][j]
            for k in k_vectors:
                x = i - k[0]
                y = j - k[1]
                if x >= 0 and y >= 0:  # we can make a step from (x, y) point
                    max_sum = max(max_sum, mat[x][y] + mat[i][j])
            mat[i][j] = max_sum

    return mat[n-1][m-1]


mat = [[0, 1, 1],
       [5, 10, 1],
       [3, 1, 1]]

vec = [[0, 2], [1, 0]]

print(solution(mat, vec))
