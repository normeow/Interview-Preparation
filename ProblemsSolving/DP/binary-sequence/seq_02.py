'''
Given: N > 1, 1 <= k < 2^N
Find the number of good sequences of 0 and 1 without consecutive 1's length N

Print k-th sequence (lexicograph sorting) len = N
'''


def solution(n, k):
    def out(ans, i, k):
        if i < 0:
            return

        if i == 0:
            if k == 1:
                print('0', end='')
            else:
                print('1', end='')
            return

        if k <= ans[i-1]:
            print('0', end='')
            out(ans, i-1, k)
        else:
            print('10', end='')
            out(ans, i-2, ans[i] - k)



    ans = [0] * n
    ans[0] = 2
    ans[1] = 3
    for i in range(2, n):
        ans[i] = ans[i-1] + ans[i-2]

    out(ans, n-1, k)


for i in range(1, 9):
    solution(4, i)
    print()
