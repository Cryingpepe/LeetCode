class Solution:
    def smallestNumber(self, n: int) -> int:
        
        result = 1

        while result - 1 < n:
            result *= 2

        return result - 1