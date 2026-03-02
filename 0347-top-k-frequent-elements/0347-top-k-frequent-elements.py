class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = collections.defaultdict(int)
        result = []

        for i in nums:
            hashmap[i] += 1

        for num, freq in hashmap.items():
            result.append([freq, num])

        result.sort()

        return [num for freq, num in result[-k:]]