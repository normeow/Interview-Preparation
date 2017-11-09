'''
additional: calculate the minimum number of coins
'''

def min_non_zero(a):
    if len(a) == 0:
        return None

    res = a[0]
    for x in a:
        if x < res and x != 0 or res == 0:
            res = x

    return res


def solution_minimize_coins(a, s):
    coins_num = len(a)
    ans_matrix = [[0] * (s + 1) for _ in range(coins_num)]
    if a[0] <= s:
        ans_matrix[0][a[0]] = 1

    for coin_i in range(1, coins_num):
        coin = a[coin_i]
        for sub_s in range(s + 1):
            res = 0
            if sub_s == coin:
                res = 1
            elif sub_s < coin:
                res = ans_matrix[coin_i - 1][sub_s]
            elif ans_matrix[coin_i - 1][sub_s - coin] != 0:
                res = ans_matrix[coin_i - 1][sub_s - coin] + 1

            ans_matrix[coin_i][sub_s] = res

    last_col = []
    for i in range(coins_num):
        last_col.append(ans_matrix[i][s])

    return min_non_zero(last_col)
