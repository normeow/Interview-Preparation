'''
https://www.hackerrank.com/challenges/greedy-florist/problem

Where is greedy algorithms can be applied here?
'''


def getMinimumCost(n, k, c):
    res = 0
    x = 0
    c.sort(reverse=True)
    i = 0
    while i < n:
        res += (x + 1)*c[i]
        i += 1
        if i % k == 0:
            x += 1
    return res


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = list(map(int, input().strip().split(' ')))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)