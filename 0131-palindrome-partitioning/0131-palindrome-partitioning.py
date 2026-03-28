class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        part = []

        def backtrack(idx):
            if idx >= n:
                result.append(part[:])
                return

            for i in range(idx, n):
                temp = s[idx : i + 1]
                
                if temp == temp[::-1]:
                    part.append(temp)
                    backtrack(i + 1)
                    part.pop()
        
        backtrack(0)
        return result