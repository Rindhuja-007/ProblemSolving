def isValid(word):
    vowels = "aeiouAEIOU"
    consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    nums="1234567890"
    if len(word) < 3:
        return False
    else:
        cons = 0
        vow = 0
        for i in word:
            if i in vowels:
                vow += 1
            elif i in consonant:
                cons += 1
            elif i in nums:
                continue
            else:
                return False
    if vow == 0 or cons == 0:
        return False
    else:
        return True

word="234ADas"
