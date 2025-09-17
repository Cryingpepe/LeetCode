class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        queue = deque()
        total = 0
        minCount = float("inf")

        for i in nums:
            queue.append(i)
            total += i

            while total >= target:
                minCount = min(minCount, len(queue))
                total -= queue.popleft()
            
        if minCount == float("inf"):
            minCount = 0

        return minCount




