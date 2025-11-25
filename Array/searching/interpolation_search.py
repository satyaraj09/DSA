"""
Interpolation search estimates the position of the target in a sorted array, 
uniformaly distributes array using formula:

pos = low + (target - arr[low])(high - low) / arr[high] - arr[low]

It then search near this estimated position instead of the middle, 
making it faster than binary search for uniform data.
"""


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:

        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            else:
                return -1

        pos = low + ((target - arr[low]) *
                     (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos

        elif arr[pos] < target:
            low += 1

        else:
            high -= 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(interpolation_search(arr, 40))
