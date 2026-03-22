class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        for x in range(4):

            if mat == target:
                return True

            mat = [list(r) for r in zip(*mat[::-1])] # Rotate 90 degrees

            # *: unpacking
            # zip: binding elements in same index ex) zip((1,2,3),(a,b,c)) = ((1,a),(2,b),(3,c))

        return False