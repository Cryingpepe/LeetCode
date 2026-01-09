class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        sumOfN = (n * (n + 1)) // 2
        sumOfRealN = sum(nums)

        return sumOfN - sumOfRealN