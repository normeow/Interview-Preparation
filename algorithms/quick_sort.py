def quick_sort(a, left, right):
    i = left
    j = right
    pivot = (i + j) // 2
    if i < j:
        while i < j:
            while a[i] < a[pivot]:
                i += 1
            while a[j] > a[pivot]:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        quick_sort(a, left, i-1)
        quick_sort(a, i, right)


def sort(a):
    quick_sort(a, 0, len(a) - 1)
    return a


def cmp(a, b):
    if len(a) != len(b):
        return False
    return sum([1 for i, j in zip(a, b) if i == j]) == len(a)


assert cmp(sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
assert cmp(sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
assert cmp(sort([2, 3, 1, 5, 4]), [1, 2, 3, 4, 5])
assert cmp(sort([]), [])
assert cmp(sort([1]), [1])
