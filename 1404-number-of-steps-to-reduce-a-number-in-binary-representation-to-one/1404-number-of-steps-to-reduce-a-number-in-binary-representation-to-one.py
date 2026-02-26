class Solution:
    def numSteps(self, s: str) -> int:
        
        result = 0

        s = int(s, 2)

        while s > 1:
            
            if s & 1:
                s += 1
            else:
                s >>= 1
            
            result += 1
        
        return result
        
