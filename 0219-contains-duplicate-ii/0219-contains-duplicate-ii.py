class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        hashMap = {}

        for i, num in enumerate(nums):
            if num not in hashMap:
                hashMap[num] = i
            else:
                if abs(hashMap[num] - i) <= k:
                    return True
                hashMap[num] = i
        
        return False

        