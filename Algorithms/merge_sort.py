def merge_sort(a, left, right):
    if left < right:
        mid = (right + left) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        merge_halves(a, left, right)


def merge_halves(a, left_start, right_end):
    left_end = (left_start + right_end) // 2
    right_start = left_end + 1

    size = right_end - left_start + 1
    temp = [0] * size

    left = left_start
    right = right_start

    i = 0
    while left <= left_end and right <= right_end:
        if a[left] < a[right]:
            temp[i] = a[left]
            left += 1
        else:
            temp[i] = a[right]
            right += 1
        i += 1

    if left <= left_end:
        temp[i:] = a[left:left_end + 1]
    elif right <= right_end:
        temp[i:] = a[right:right_end + 1]

    a[left_start:right_end + 1] = temp[:]


def sort(a):
    merge_sort(a, 0, len(a) - 1)
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
