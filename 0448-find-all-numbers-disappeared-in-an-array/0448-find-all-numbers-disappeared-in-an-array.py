class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # hashmap = {}
        # result = []

        # for i in range(len(nums)):
            
        #     hashmap[i + 1] = 0

        # for i in range(len(nums)):

        #     hashmap[nums[i]] += 1

        # for i in hashmap.keys():

        #     if hashmap[i] == 0:

        #         result.append(i)

        # return result

        result = []

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
                

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
                
        return result

