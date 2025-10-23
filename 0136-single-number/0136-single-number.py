class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hashMap = Counter(nums)

        for i in nums:
            if hashMap[i] == 1:
                return i