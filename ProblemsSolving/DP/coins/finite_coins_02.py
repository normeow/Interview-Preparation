'''
Given:
coins a1, a2 ... an
sum S > 0

Can we collect sum s from coins using each only once?

'''

'''
improvements:
1. to save memory use not the whole matrix, but the last two rows of it
2. use one additional first row: coin = 0 
'''

def solution(a, s):
    coins_num = len(a)
    prev = [0] * (s + 1)
    cur = prev.copy()
    prev[0] = 1

    for coin_i in range(0, coins_num):
        for sub_s in range(s + 1):
            cur[sub_s] = prev[sub_s]
            if sub_s >= a[coin_i]:
                cur[sub_s] = prev[sub_s] or prev[sub_s - a[coin_i]]
        prev = cur.copy()

    print(cur)

    return cur[s] == 1



