class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
        result = []
        num = 0

        for i in range(len(nums)):
            num = (num << 1) + nums[i]
            
            if num % 5 == 0:
                result.append(True)
            else:
                result.append(False)

        return result