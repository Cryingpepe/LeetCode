class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
        result = [False for _ in range(len(nums))]
        num = 0

        for i in range(len(nums)):
            num = (num << 1) + nums[i]
            
            if num % 5 == 0:
                result[i] = True
            else:
                result[i] = False

        return result