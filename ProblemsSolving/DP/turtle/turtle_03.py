'''
Given: matrix nxm, 0 < k < number of ways
turtle moves from left-bottom (0,0) corner to right-bottom (n-1, m-1) and each step is step to the RIGHT or UP
print k-th path
'''


def solution(n, m, k):
    def out(mat, i, j, k):
        if i == j == 0:
            return
        if i == 0:
            print('R'*j, end='')
        elif j == 0:
            print('U'*i, end='')
        elif k <= mat[i][j-1]:
            print('R', end='')
            out(mat, i, j-1, k)
        else:
            print('U', end='')
            out(mat, i-1, j, k - mat[i][j-1])

    mat = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                mat[i][j] = 1
            else:
                mat[i][j] = mat[i-1][j] + mat[i][j-1]

    out(mat, n-1, m-1, k)


mat = [[1, 1, 1],
       [1, 2, 3],
       [1, 3, 6]]


for i in range(1,7):
    solution(3, 3, i)
    print()





