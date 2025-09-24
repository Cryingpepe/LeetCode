class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = sorted(nums1 + nums2)
        length = len(nums)

        if length % 2 == 1:
            median = nums[length // 2]
        else:
            median = (nums[length // 2 - 1] + nums[length // 2]) / 2

        return median