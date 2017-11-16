'''
Given: matrix nxm
turtle moves from left-bottom (0,0) corner to right-bottom (n-1, m-1) and each step is step to the RIGHT or UP
String S = {'R', 'D'}* -- way of turtle from (0,0) () to (n-1, m-1)

Find the No. k of its way (if all ways sorted)
'''


def solution(way, n, m):
    def get_num(ans, way, i, j):
        if way == '':
            return 0


        if way[0] == 'R':
            return get_num(ans, way[1:], i, j-1)
        else:
            if j == 0:
                return get_num(ans, way[1:], i-1, j)
            else:
                return ans[i][j-1] + get_num(ans, way[1:], i-1, j)

    mat = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                mat[i][j] = 1
            else:
                mat[i][j] = mat[i-1][j] + mat[i][j-1]

    return get_num(mat, way, n-1, m-1) + 1


mat = [[1, 1, 1],
       [1, 2, 3],
       [1, 3, 6]]

ways = [
        'RRUU',
        'RURU',
        'RUUR',
        'URRU',
        'URUR',
        'UURR'
        ]

for way in ways:
    print(solution(way, 3, 3))





