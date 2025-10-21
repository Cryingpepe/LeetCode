class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def backtrack(num):
            if num == len(nums):
                result.append(nums[:])
                return

            for i in range(num, len(nums)):
                temp = nums[num]
                nums[num] = nums[i]
                nums[i] = temp

                backtrack(num + 1)

                temp = nums[num]
                nums[num] = nums[i]
                nums[i] = temp

        backtrack(0)

        return result
                
            