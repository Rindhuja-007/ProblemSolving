def containsNearbyDuplicate(nums,k):
    index_map = {}
    for i, num in enumerate(nums):
        if num in index_map:
            if i - index_map[num] <= k:
                return True
        index_map[num] = i

    return False


nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums,k))
