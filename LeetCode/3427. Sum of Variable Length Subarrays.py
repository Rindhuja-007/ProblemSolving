from itertools import accumulate

def subarray_sum(nums):
    s = list(accumulate(nums, initial=0))
    return sum(s[i + 1] - s[max(0, i - x)] for i, x in enumerate(nums))


nums = [2, 3, 1 ]
print(subarray_sum(nums))  
