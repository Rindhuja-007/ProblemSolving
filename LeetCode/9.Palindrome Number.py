class Solution:
    def isPalindrome(self, x):
       if x<0:
        print("false")

       y=x
       rev=0
       while y>0:
          rem=y%10
          rev=rev*10+rem
          y =y//10
       return x==rev

      
