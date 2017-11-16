'''

https://www.hackerrank.com/challenges/coin-change/problem
solution accepted

Given:
coins a1, a2 ... an
sum S > 0

How many ways to collect sum s from coins if each coin is available in an infinite quantity?


'''


def solution(c, n):
    mat = [[0] * (n + 1) for _ in range(len(c))]
    for i in range(n+1):
        if i % c[0] == 0:
            mat[0][i] = 1

    for coin_i in range(1,len(c)):
        coin = c[coin_i]
        for sub_s in range(n+1):
            mat[coin_i][sub_s] = mat[coin_i-1][sub_s]
            if coin <= sub_s:
                prev_s = sub_s - coin
                while prev_s >= 0:
                    mat[coin_i][sub_s] += mat[coin_i-1][prev_s]
                    prev_s -= coin
    return mat[-1][-1]


s = 3
c = [8, 3, 1, 2]

print(solution(c, s))
