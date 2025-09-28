# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        nums = []

        def dfs(root, numSum):
            if not root.left and not root.right:
                numSum = numSum*10 + root.val
                nums.append(numSum)
            
            if root.left:
                dfs(root.left, numSum*10 + root.val)
            if root.right:
                dfs(root.right, numSum*10 + root.val)
            
            return
        
        dfs(root, 0)

        return sum(nums)
        