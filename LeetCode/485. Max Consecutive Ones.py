def findmax(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 0

    max_count = max(max_count, current_count)

    return max_count


nums=[0,1,1,1]
print(findmax(nums))
