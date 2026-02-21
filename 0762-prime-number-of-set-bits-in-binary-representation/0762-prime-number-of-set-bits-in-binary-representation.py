class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        def isPrime(n):

            if n < 2:
                return False

            for i in range(2, int(math.sqrt(n)) + 1):

                if n % i == 0:

                    return False

            return True

        result = 0
        
        for i in range(left, right + 1):
            
            bits = bin(i).count('1')
            
            if isPrime(bits):
                print(i)
                result += 1
        
        return result
        
        