class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        result = []
        
        for n in nums:
            
            if n != 2:
                result.append(n - ((n + 1) & (-n - 1)) // 2)
            else:
                result.append(-1)

        return result