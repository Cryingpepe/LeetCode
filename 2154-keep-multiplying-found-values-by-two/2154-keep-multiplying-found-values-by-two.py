class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        numdict = Counter(nums)

        while original in numdict:
            original *= 2

        return original