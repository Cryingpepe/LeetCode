class Solution(object):
    def fib(self, n):
        
        fibonacciList = [0, 1, 1] 

        for i in range(3, n+1):
            fibonacciList.append(fibonacciList[i-1] + fibonacciList[i-2])
    
        return fibonacciList[n]
    

        