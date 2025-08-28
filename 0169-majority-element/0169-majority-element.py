class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictForElements = {}

        for i in nums:
            if i not in dictForElements:
                dictForElements[i] = 1
            else:
                dictForElements[i] += 1

        return max(dictForElements, key = dictForElements.get) 