class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        minNum = min(nums)
        maxNum = max(nums)
        result = []
        
        for i in range(minNum, maxNum):
            if i not in nums:
                result.append(i)

        return result