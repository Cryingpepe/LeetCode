class Solution(object):
    def climbStairs(self, n):
        
        wayToNList = [1, 1] # base case: there is 1 way to go 0th stair and 1 way to go 1st stair 

        for i in range(2, n+1):
            wayToNList.append(wayToNList[i-1] + wayToNList[i-2]) # since there are always two ways to get n (2 steps from n-2 or 1 step from n-1)
    
        return wayToNList[n]
    

        