class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mdict={}
        rdict={}

        for i in ransomNote:
            if i in rdict:
                rdict[i]+=1
            else:
                rdict[i]=1
        for j in magazine:
            if j in mdict:
                mdict[j]+=1
            else:
                mdict[j]=1

        for i in rdict:
            if i in mdict and rdict[i]<=mdict[i]:
                continue
            else:
                return False

        return True
