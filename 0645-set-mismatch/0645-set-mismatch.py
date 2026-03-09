class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        count = [0] * (len(nums))

        for i in range(len(nums)):
            count[nums[i] - 1] += 1

        i = count.index(2) + 1
        j = count.index(0) + 1

        return [i,j]

            
            
        