class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        count1 = 0
        count0 = 0

        for i in nums[::-1]:
            if count1 == 2:
                return False
            if count0 >= k:
                return True
        
            if i == 1:
                count1 += 1
            else:
                count0 += 1

        if count1 == 1:
            return True
        else:
            return False

