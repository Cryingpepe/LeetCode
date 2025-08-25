class Solution(object):
    def removeDuplicates(self, nums):
        start = 0
        count = 0

        while start < len(nums):
            if start + 1 < len(nums) and nums[start] == nums[start + 1] and nums[start] != 101:
                nums.pop(start)
                nums.append(101)
            else:
                if nums[start] != 101:
                    count += 1
                start += 1

        return count
