def countsegments(s):
    count=0
    if len(s) == 0 or s.isspace():
        return 0
    else:
        words = s.split(" ")
        for i in words:
            if i !="":
                count+= 1

    return count

s="hi rin,   "
ans=countsegments(s)
print(ans)
