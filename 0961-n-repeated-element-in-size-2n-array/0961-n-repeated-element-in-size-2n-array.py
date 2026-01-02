class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        freq = {}
        
        for i in nums:
            if i not in freq:
                freq[i] = 0
            else:
                return i
