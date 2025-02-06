def isBalanced(num):
    even = 0
    odd=0
    n = len(num)
    for i in range(0, n, 2):
        even += (int(num[i]))
    for i in range(1,n,2):
        odd+=(int(num[i]))

    if even==odd:
        return True

    else:
        return False

num="24123"
ans=isBalanced(num)
print(ans)
