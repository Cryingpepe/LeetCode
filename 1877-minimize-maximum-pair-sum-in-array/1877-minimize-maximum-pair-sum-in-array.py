class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()

        pairSum = []

        for i in range(len(nums) // 2):
            pairSum.append(nums[i] + nums[(-1) - i])
        
        return max(pairSum)