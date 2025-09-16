class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        stepsToN = [1, 1] # 1 way to 0th and 1st stairs

        for i in range(2, n + 1):
            stepsToN.append(stepsToN[i-2] + stepsToN[i-1])

        return stepsToN[n]

