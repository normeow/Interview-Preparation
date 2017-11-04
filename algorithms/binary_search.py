def binary_search(a, x):
    left = 0
    right = len(a)
    while left != right:
        mid = (left + right) // 2
        if a[mid] > x:  # x in the left half
            right = mid
        elif a[mid] < x:  # x in the right half
            left = mid + 1
        else:
            return mid

    return -1

a = [1,2,3,4]
assert(binary_search(a, 1) == 0)
assert(binary_search(a, 4) == 3)
assert(binary_search(a, 5) == -1)
assert(binary_search(a, 2) == 1)

a = [1,2,3,4,5]
assert(binary_search(a, 5) == 4)
assert(binary_search(a, 1) == 0)
assert(binary_search(a, 3) == 2)



