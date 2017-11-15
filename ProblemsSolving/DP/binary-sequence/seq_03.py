'''
Given: N > 1, a = a1..a2 -- binary sequence without consecutive 1's length N
Find: no. k of se lexicograph sorting

i.e.
n = 3, a = 010 => k = 3
explanation:

000 -- k = 1
001 -- k = 2
010 -- k = 3
100 -- k = 4
101 -- k = 5
'''


def solution(a):
    def get_no(ans, a, i):
        if i < 0:
            return 0

        first_elem_index = len(a) - i - 1
        if i == 0:
            if a[first_elem_index] == '0':
                return 1
            else:
                return 2

        if a[first_elem_index] == '0':
            return get_no(ans, a, i-1)
        else:
            if i == 1:
                return ans[i-1] + 1
            else:
                return ans[i-1] + get_no(ans, a, i-2)

    n = len(a)
    ans = [0] * n
    ans[0] = 2
    ans[1] = 3
    for i in range(2, n):
        ans[i] = ans[i-1] + ans[i-2]

    return get_no(ans, a, n - 1)


print(solution('000'))
