'''
Given:
coins a1, a2 ... an
sum S > 0

Can we collect sum s from coins using each only once?

'''


def solution(a, s):
    coins_num = len(a)
    ans_matrix = [[0] * (s + 1) for _ in range(coins_num)]
    ans_matrix[0][0] = 1
    if a[0] <= s:
        ans_matrix[0][a[0]] = 1

    for coin_i in range(1, coins_num):
        for sub_s in range(s + 1):
            ans_matrix[coin_i][sub_s] = ans_matrix[coin_i - 1][sub_s]
            if sub_s >= a[coin_i]:
                ans_matrix[coin_i][sub_s] = ans_matrix[coin_i][sub_s] or ans_matrix[coin_i - 1][sub_s - a[coin_i]]

    print(ans_matrix)

    for i in range(coins_num):
        if ans_matrix[i][s]:
            return True

    return False



