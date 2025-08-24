class Solution(object):
    def removeElement(self, nums, val):
        
        x = 0
        count = 0

        while (1):

            try:
                if (nums[x] == val):
                    nums.pop(x)
                    nums.append(101)
                else:
                    if nums[x] != 101:
                        count += 1
                    x += 1
            
            except:
                break

        return count
