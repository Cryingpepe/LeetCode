class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        result = sum(nums)
        minheap1 = []
        minheap2 = []

        for i in range(len(nums)):
            if nums[i] % 3 == 1:
                heapq.heappush(minheap1, nums[i])
            elif nums[i] % 3 == 2:
                heapq.heappush(minheap2, nums[i])

        if result % 3 == 0:
            return result

        elif result % 3 == 1:

            dummy = result

            while dummy % 3 != 0:
                if not minheap2:
                    dummy = 0
                    break
                dummy = dummy - heapq.heappop(minheap2)

            return max(result - heapq.heappop(minheap1), dummy)

        elif result % 3 == 2:
            
            dummy = result

            while dummy % 3 != 0:
                if not minheap1:
                    dummy = 0
                    break
                dummy = dummy - heapq.heappop(minheap1)

            return max(result - heapq.heappop(minheap2) if minheap2 else dummy, dummy)