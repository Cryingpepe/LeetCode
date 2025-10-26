class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def dfs(left, right, parentheses):

            if len(parentheses) == n * 2:
                result.append(parentheses)
                return 

            if left < n:
                dfs(left + 1, right, parentheses + '(')

            if right < left:
                dfs(left, right + 1, parentheses + ')')

        dfs(0, 0, '')

        return result