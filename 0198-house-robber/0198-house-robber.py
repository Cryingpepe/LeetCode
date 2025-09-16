class Solution(object):
    def rob(self, nums):

        n = len(nums)

        if n < 3:    # if n is less than 3, it can be caluated with the base cases
            return max(nums)
        elif n == 3:      # if n is equal to 3, than there is only one addition needed
            nums[2] = nums[2] + nums[0]
            return max(nums)
        else:       # else, set base case for index 2
            nums[2] = nums[2] + nums[0]    

        for i in range(3, n):
            
            nums[i] = nums[i] + max(nums[i-2], nums[i-3])
        
        return max(nums[n-1], nums[n-2])
        