class Solution(object):
    def isPalindrome(self, x):

        start = 0
        end = -1

        x = str(x)
        length = len(x)
        
        if length < 2:
            return True

        for i in range(length / 2 + 1):
            if x[start] != x[end]:
                return False
            start += 1
            end -= 1
        
        return True
        

        # if x < 0:
        #     return False
        # elif x < 10:
        #     return True

        # else:

        #     while x > 0:
        #         xx = x
        #         count = 0  
        #         a = x % 10

        #         while int(xx) >= 10:
        #             count += 1
        #             xx /= 10

        #         xx = int(xx) 
                
        #         if xx != a:
        #             return False
        #         else:
        #             x -= a
        #             x -= xx * 10**count
        #             if (x % 10 == 0) and (x / 10 != 0):
        #                 return False
        #             else:
        #                 x = int (x / 10)

        # return True