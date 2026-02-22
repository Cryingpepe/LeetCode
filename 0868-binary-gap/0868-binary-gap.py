class Solution:
    def binaryGap(self, n: int) -> int:
        
        result = 0
        count = 0

        while not(n & 1):
            n >>= 1

        while n > 0:
            if n & 1:
                result = max(count, result)
                count = 1
            else:
                count += 1
            
            n >>= 1
        
        return result
        

