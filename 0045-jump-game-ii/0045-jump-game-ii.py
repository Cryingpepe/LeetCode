class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxReach = 0
        count = 0
        maxList = []

        for i, num in enumerate(nums):
            
            if maxReach >= len(nums) - 1:
                return count

            if maxReach < i + num and maxReach > i:
                maxList.append(i + num)
            elif maxReach < i + num and maxReach <= i:
                maxList.append(i + num)
                maxReach = max(maxList)
                count += 1


            