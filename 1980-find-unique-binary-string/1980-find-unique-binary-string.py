class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums[0])

        if n == 1:
            return '0' if nums[0] == '1' else '1'

        for i in range(n**2):

            binary = bin(i)[2:].zfill(n)

            if binary not in nums:
                return binary
