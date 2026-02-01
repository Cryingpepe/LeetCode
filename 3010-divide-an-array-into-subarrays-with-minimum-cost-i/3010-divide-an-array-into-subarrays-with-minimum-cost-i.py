class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        result = 0

        result += nums.pop(0)
        nums.sort()

        result += nums[0] + nums[1]


        return result

