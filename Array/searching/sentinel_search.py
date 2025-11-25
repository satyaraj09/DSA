def sentinel_search(nums, target):
    last = nums[-1]
    nums[-1] = target
    
    i = 0
    
    while nums[i] != target:
        i += 1
        
    nums[-1] = last
    
    if i < len(nums) - 1 or nums[-1] == target:
        return i
    else:
        return -1
    
arr = [1, 5, 2, 4, 3, 7, 9, 8]
print(sentinel_search(arr, 9))