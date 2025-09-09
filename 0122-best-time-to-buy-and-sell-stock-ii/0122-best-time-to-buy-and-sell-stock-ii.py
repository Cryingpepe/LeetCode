class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        stock = 100000
        
        for i in prices:
            if i <= stock:
                stock = i
            else:
                profit += (i - stock)
                stock = i
        
        return profit
            