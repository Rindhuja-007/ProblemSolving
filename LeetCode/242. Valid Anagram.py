class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for i in s:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        
        for j in t:            
            if j in dict2:
                dict2[j]+=1
            else:
                dict2[j]=1


        for i in dict1:
            if i in dict2 and dict1[i]==dict2[i] and len(dict2)==len(dict1):
                continue
            else:
                return False
        return True
