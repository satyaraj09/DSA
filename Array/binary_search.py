def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return - 1

arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 9))
