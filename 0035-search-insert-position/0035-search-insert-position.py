class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        length = len(nums)

        if nums[length // 2] < target:
            if length == 1:
                return 1
            return self.searchInsert(nums[(length // 2):], target) + (length // 2)

        elif nums[length // 2] > target:
            if length == 1:
                return 0
            return self.searchInsert(nums[:(length // 2)], target)

        else:
            return length // 2