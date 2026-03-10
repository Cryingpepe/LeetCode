class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        hashmap = {}
        result = []

        for i in range(len(nums)):
            
            hashmap[i + 1] = 0

        for i in range(len(nums)):

            hashmap[nums[i]] += 1

        for i in hashmap.keys():

            if hashmap[i] == 0:

                result.append(i)

        return result