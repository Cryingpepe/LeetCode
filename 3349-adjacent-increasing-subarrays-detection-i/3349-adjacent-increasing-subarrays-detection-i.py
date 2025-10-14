class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
 

        increasing = 1
        prevIncreasing = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing += 1
            else:
                prevIncreasing = increasing
                increasing = 1

            if increasing // 2 >= k or min(prevIncreasing, increasing) >= k:
                return True

        return False

        
