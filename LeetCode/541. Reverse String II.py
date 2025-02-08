
def reverseStr(s, k):
    ans = []
    n = len(s)

    for i in range(0, n, 2 * k):
        reverse = s[i:i + k][::-1]
        keep = s[i + k:i + 2 * k]
        ans.append(reverse+keep)
    return ''.join(ans)


s = "abcdefg"
k = 2
print(reverseStr(s, k))
