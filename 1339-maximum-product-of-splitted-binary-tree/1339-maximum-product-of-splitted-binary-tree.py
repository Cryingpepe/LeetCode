# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        sums = []

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            s = node.val + left + right
            sums.append(s)
            return s
        
        total = dfs(root)
        result = 0

        for s in sums:
            result = max(result, s * (total - s))
        
        return result % (10 ** 9 + 7)