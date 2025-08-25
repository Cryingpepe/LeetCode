class Solution(object):
    def removeDuplicates(self, nums):

        start = 0
        count = 0

        while (1):
            try:
                if nums[start] == nums[start + 1] and nums[start] is not 101:
                    nums.pop(start)
                    nums.append(101)
                else:

                    if nums[start] is not 101:
                        count += 1

                    start += 1
            except:
                if nums[-1] != 101:
                    count += 1
                
                break
        
        return count