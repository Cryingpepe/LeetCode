class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        result = []

        if len(matrix[0]) == 1:
            for i in matrix:
                result += i
            return result

        while matrix:

            result += matrix[0]
            matrix.pop(0)

            if not matrix:
                break

            for i in matrix:
                result.append(i.pop())
                if not i:
                    matrix.remove(i)

            if not matrix:
                break

            for i in matrix[-1][::-1]:
                result.append(i)
            matrix.pop()

            if not matrix:
                break
            
            for i in matrix[::-1]:
                result.append(i.pop(0))
                if not i:
                    matrix.remove(i)
            
            if not matrix:
                break


        return result

            
            
            
