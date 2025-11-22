# Linear Search:
# Scan the list from start to end.
# Compare each item to the target.
# Stop if found; if you reach the end, it's not in the list.

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

array = [2, 6, 4, 1, 8, 5, 9, 7]
print(linear_search(array, 1))
