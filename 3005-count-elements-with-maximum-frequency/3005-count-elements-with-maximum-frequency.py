class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hashMap = {}
        count = 0
        maxValue = 0

        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1

        for i in hashMap.values():
            if i > maxValue:
                maxValue = i
                count = 1
            elif i == maxValue:
                count += 1
        
        return count * maxValue
            