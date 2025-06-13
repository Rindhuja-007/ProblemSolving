def solution(s):
    new_s = []
    i = 0
    while i < len(s):
        if i + 1 < len(s):
            new_s.append(s[i] + s[i+1])
        else:
            new_s.append(s[i] + '_')
        i += 2
    return new_s
