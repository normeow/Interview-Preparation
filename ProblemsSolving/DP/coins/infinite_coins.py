'''
Given:
coins a1, a2 ... an
sum S > 0

Can we collect sum s from coins if each coin is available in an infinite quantity?

'''


def solution(a, s):
    coins_num = len(a)
    ans_matrix = [[0] * (s + 1) for _ in range(coins_num)]

    # from first coin we can collect any sum that is divisible by coin
    for i in range(s + 1):
        if i % a[0] == 0:
            ans_matrix[0][i] = 1

    for coin_i in range(1, coins_num):
        for sub_s in range(s+1):
            ans_matrix[coin_i][sub_s] = ans_matrix[coin_i - 1][sub_s]
            temp_s = sub_s
            while temp_s >= a[coin_i]:
                temp_s -= a[coin_i]
                ans_matrix[coin_i][sub_s] = ans_matrix[coin_i][sub_s] or ans_matrix[coin_i - 1][temp_s]

    for i in range(coins_num):
        if ans_matrix[i][s]:
            return True

    return False
