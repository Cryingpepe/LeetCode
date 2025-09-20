class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        collection = set()

        def logic(num):
            result = 0

            while num != 0:
                firstDigit = num % 10
                result += firstDigit ** 2
                num = num // 10
            
            return result
        
        while n not in collection:
            collection.add(n)
            n = logic(n)
            
            if n == 1:
                return True
        
        return False

