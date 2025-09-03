class Solution(object):

    def binarySearch(self, matrix, target):
        
        left, right = 0, len(matrix) - 1

        while right >= left:
            mid  = (left + right) // 2

            if matrix[mid] == target:
                return True
            elif matrix[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False




    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for i in matrix:
            if i[0] <= target <= i[-1]:  
                return self.binarySearch(i, target)
        
        return False

        