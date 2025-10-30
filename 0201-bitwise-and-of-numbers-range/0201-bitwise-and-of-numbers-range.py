class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        move = 0
        
        while left < right:
            left >>= 1
            right >>= 1
            move += 1
        
        return left << move