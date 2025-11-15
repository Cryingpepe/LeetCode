class Solution(object):
    def generate(self, numRows):
        
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        dp = [[1], [1, 1]]

        for _ in range(numRows - 2):
            prev = dp[-1]
            row = [1]

            for i in range(len(prev) - 1):
                row.append(prev[i] + prev[i + 1])

            row.append(1)
            dp.append(row)

        return dp
