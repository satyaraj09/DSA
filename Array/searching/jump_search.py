# Jump Search works on sorted arrays.
# Instead of checking every element, it jumps ahead by fixed steps usually(sqrt(n))

import math


def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1


arr = [2, 5, 8, 12, 14, 19, 23, 27, 30, 35]
print(jump_search(arr, 12))
