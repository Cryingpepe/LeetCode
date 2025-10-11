class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = 0
        result = []
        zeros = 0

        for i in nums:
            if i == 0:
                zeros += 1

        if zeros < 2:
            
            for i in nums:    
                if i != 0 and total != 0:
                    total *= i
                elif i != 0 and total == 0:
                    total += i
        
        if 0 in nums:
            for i in nums:
                if i == 0:
                    result.append(total)
                else:
                    result.append(0)
        else:
            for i in nums:
                result.append(total // i)
        
        return result