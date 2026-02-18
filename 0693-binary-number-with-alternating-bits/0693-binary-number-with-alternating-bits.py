class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        if n & 1 == 1:
            while n > 0:
                if not(n & 1):
                    return False

                n >>= 1

                if n <= 0:
                    break

                if n & 1:
                    return False
                
                n >>= 1

        else:
            while n > 0:
                if n & 1:
                    return False

                n >>= 1

                if n <= 0:
                    break

                if not(n & 1):
                    return False
                
                n >>= 1
        
        return True
