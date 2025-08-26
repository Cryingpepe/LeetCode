import math

class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        maximumDiagonal = 0
        result = 0

        for i in range(len(dimensions)):
            x = dimensions[i][0]
            y = dimensions[i][1]
            z = math.sqrt(x * x + y * y)

            if maximumDiagonal < z:
                maximumDiagonal = z
                result = x * y
            elif z == maximumDiagonal:
                result = max(result, x * y)
        
        return result
