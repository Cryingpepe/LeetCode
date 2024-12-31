class Solution(object):
    def tribonacci(self, n):
        
        tribonacciList = [0, 1, 1]

        for i in range(3, n + 1):
            tribonacciList.append(tribonacciList[i - 1] + tribonacciList[i - 2] + tribonacciList[i - 3])
    
        return tribonacciList[n]