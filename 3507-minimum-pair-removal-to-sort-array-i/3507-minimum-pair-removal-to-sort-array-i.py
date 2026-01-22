class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        result = 0

        def is_sorted(arr):

            for i in range(len(arr) - 1):

                if arr[i] > arr[i + 1]:
                    return False

            return True

        while not is_sorted(nums):
            pair_sums = [nums[i] + nums[i + 1] for i in range(len(nums) - 1)]

            min_sum = min(pair_sums)
            idx = pair_sums.index(min_sum)
            nums[idx] = min_sum
            nums.pop(idx + 1)
            result += 1

        return result