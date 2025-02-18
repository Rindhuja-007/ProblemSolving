def findDisappearedNumbers(nums):
    ans=[]
    snums=set(nums)
    for i in range(1,len(nums)+1):
        if i not in snums:
            ans.append(i)

    return ans



nums=[4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))
