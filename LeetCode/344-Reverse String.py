class Solution(object):
    def reverseString(self, s):
        l=0
        n=len(s)-1
        while l<n:
            s[l],s[n]=s[n],s[l]
            l=l+1
            n=n-1
        return s
        
        
        
