import math
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        l=len(set(candyType))
        k=int(len(candyType)/2)
        return l if l<k else k

        
