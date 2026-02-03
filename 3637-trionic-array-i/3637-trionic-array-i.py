class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        idx =  0

        while idx + 1 < len(nums) and nums[idx] < nums[idx + 1]:
            idx += 1

        if idx == 0 or idx == len(nums) - 1: 
            return False
        
        idx2 = idx

        while idx + 1 < len(nums) and nums[idx] > nums[idx + 1]: 
            idx += 1
        
        if idx == idx2 or idx == len(nums) - 1: 
            return False
        
        while idx + 1 < len(nums) and nums[idx] < nums[idx + 1]: 
            idx += 1

        return idx == len(nums) - 1