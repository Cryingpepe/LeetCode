class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                # The peak is at mid or to its left
                right = mid
            else:
                # The peak is to the right of mid
                left = mid + 1
        
        # When left == right, we have found a peak element
        return left