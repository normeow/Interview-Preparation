'''
Given sequence: a1... an of integer numbers
Get increasing subsequence, striking out the minimum number of elements
Return the length of subsequence

i.e.
input: 1 3 3 1 4 2
output: 3 (max subsequence is 1 3 4)

the idea:
ans[i] keep len of max subsequence of a1...ai with condition: we cannot strike out a[i]
'''


def solution(a):
    if len(a) == 0:
        return 0

    n = len(a)
    ans = [0] * n
    ans[0] = 1
    for i in range(n):
        ans[i] = 1
        a_max = 0
        for j in range(i):
            if a[j] < a[i] and ans[j] > a_max:
                a_max = ans[j]
        ans[i] += a_max

    return max(ans)


assert solution([1, 3, 3, 1, 4, 2]) == 3
assert solution([]) == 0
assert solution([2]) == 1
assert solution([5, 4, 3, 2, 1]) == 1