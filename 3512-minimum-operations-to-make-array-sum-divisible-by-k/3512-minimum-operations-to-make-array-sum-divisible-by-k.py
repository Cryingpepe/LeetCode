class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        sumOfNums = sum(nums)

        return sumOfNums % k