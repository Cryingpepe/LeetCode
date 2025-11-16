class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        dp = [[1], [1, 1]]

        for _ in range(rowIndex - 1):
            prev = dp[-1]
            row = [1]

            for i in range(len(prev) - 1):
                row.append(prev[i] + prev[i + 1])

            row.append(1)
            dp.append(row)

        return dp[-1]