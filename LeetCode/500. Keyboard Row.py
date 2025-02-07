
def findWords(words):
    first = "QWERTYUIOPqwertyuiop"
    second = "ASDFGHJKLasdfghjkl"
    third = "ZXCVBNMzxcvbnm"

    ans = [0]

    for j in words:
        c1 = 0
        c2 = 0
        c3 = 0

        l = len(j)
        for i in j:
            if i in first:
                c1 += 1
            elif i in second:
                c2 += 1
            elif i in third:
                c3 += 1

        if c1 == l:
            ans.append(j)
        elif c2 == l:
            ans.append(j)
        elif c3 == l:
            ans.append(j)

    return ans[1:]

words=["Hello","Alashka","Dad","peace"]
ans=findWords(words)
print(ans)
