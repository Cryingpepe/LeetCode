class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        result = []

        if not nums:
            return result

        prev = nums[0]
        start = prev


        for i in nums[1:]:
            if (i - prev) != 1:
                if prev == start:
                    result.append(str(prev))

                else:
                    result.append(str(start) + "->" + str(prev))
                
                prev = i
                start = i

            else:
                prev = i

        if prev == start:
            result.append(str(prev))
        else:
            result.append(str(start) + "->" + str(prev))
        
        return result
            

