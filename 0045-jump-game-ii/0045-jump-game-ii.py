class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        maxIdx = 0
        maxReach = 0
        
        for i in range(len(nums) - 1):

            maxReach = max(maxReach, i + nums[i])
            
            if i == maxIdx:
                count += 1
                maxIdx = maxReach
        
        return count

            