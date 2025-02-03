class Solution(object):
    def generateParenthesis(self, n):
        result=[]

        def backtrack(s,open_bracket,close_bracket):
            if len(s)==2*n:
                result.append(s)
                return result
            
            if open_bracket<n:
                backtrack(s+"(",open_bracket+1,close_bracket)
            
            if close_bracket<open_bracket:
                backtrack(s+")",open_bracket,close_bracket+1)
        
        backtrack("",0,0)
        return result



        
        
