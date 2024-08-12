class Solution:                                               #defining a class called Solution (class name should start with capital)
    def twoSum(self,nums,target):                             # function named twoSum with parameters num(list),target(integer)
        prevmap={}                                            # dictionary called prevmap empty at first -- contains elements in the list and itws index 
        for i,n in enumerate(nums):                           # loop access the element in the num list and there index
            diff=target-n                                     # subtract a element from the target to find its pair 
            if diff in prevmap:                               # check the diff(subtracted number in the prevmap dictionary)
                return (prevmap[diff],i)                      #if its in it the return the value of key diff and our current index
            prevmap[n]=i                                      # else add the current index and its element to the prevmap
