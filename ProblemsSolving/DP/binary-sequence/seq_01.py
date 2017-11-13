'''
Given: N > 1
Find the number of good sequences length N

Good sequence -- sequence of 0 and 1 without consecutive 1's
'''


def solution(n):
    ans = [0] * n
    ans[0] = 2
    ans[1] = 3
    for i in range(2, n):
        ans[i] = ans[i-1] + ans[i-2]

    return ans[n-1]


assert solution(2) == 3
assert solution(3) == 5
