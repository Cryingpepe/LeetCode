class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        result = []
        HashMap = {}

        for num in nums:
            if num in HashMap:
                result.append(num)
            else:
                HashMap[num] = 1
        
        return result
            