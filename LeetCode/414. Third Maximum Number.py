def thirdMax(nums):
    ans = set(nums)
    if len(ans)<3:
        return max(ans)
    else:
        for i in range(2):
            ans.remove(max(ans))

        return max(ans)


nums = [1,1]
print(thirdMax(nums))
