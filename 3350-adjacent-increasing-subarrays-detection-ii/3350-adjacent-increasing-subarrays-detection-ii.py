class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        increasing = 1
        prevIncreasing = 0
        maxIncreasing = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing += 1
            else:
                maxIncreasing = max(maxIncreasing, increasing // 2, min(increasing, prevIncreasing))
                prevIncreasing = increasing
                increasing = 1

        # 마지막 구간도 비교
        maxIncreasing = max(maxIncreasing, increasing // 2, min(increasing, prevIncreasing))
        return maxIncreasing

