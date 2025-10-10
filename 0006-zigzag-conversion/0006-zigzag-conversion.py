class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s

        lines = ["" for _ in range(numRows)]
        count = 0
        isInverse = True

        for i in range(len(s)):
            lines[count] += (s[i])

            if (count == 0 or count == numRows - 1):
                isInverse = not isInverse

            if not isInverse:
                count += 1
            else:
                count -= 1
        
        return ''.join(lines)

            

