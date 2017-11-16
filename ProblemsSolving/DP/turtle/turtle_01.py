'''
Given: matrix nxm where each (i,j) is integer non-negative number
turtle moves from left-top corner to right-bottom and each step is step to the RIGHT or DOWN

Find the maximum sum the turtle can collect on its way and print all steps that turtles takes to reach it
And there is now way to collect equal sum by different steps
'''


def solution(mat):
    def out(i,j):
        if i == j == 0:
            return

        if i == 0:
            out(i, j - 1)
            print('R')
        elif j == 0:
            out(i-1, j)
            print('D')
        elif mat[i-1][j] > mat[i][j-1]:
            out(i-1, j)
            print('D')
        elif mat[i-1][j] < mat[i][j-1]:
            out(i, j-1)
            print('R')

    n = len(mat)
    m = len(mat[0])

    steps = [ [0, 1],  # down
              [1, 0]]  # right
    for i in range(n):
        for j in range(m):
            if i == j == 0:
                continue
            max_sum = mat[i][j]
            for step in steps:
                x = i - step[0]
                y = j - step[1]
                if x >= 0 and y >= 0:  # we can make a step from (x, y) point
                    max_sum = max(max_sum, mat[x][y] + mat[i][j])
            mat[i][j] = max_sum

    out(n-1, m-1)
    return mat[n-1][m-1]


mat = [[0, 1, 1],
       [5, 10, 1],
       [3, 3, 1]]



print(solution(mat))
