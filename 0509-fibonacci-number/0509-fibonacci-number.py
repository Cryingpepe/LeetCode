class Solution(object):
    def fib(self, n):
        
        fibonacciList = [1, 1] 

        for i in range(2, n+1):
            fibonacciList.append(fibonacciList[i-1] + fibonacciList[i-2])
    
        return fibonacciList[n-1]
    

        