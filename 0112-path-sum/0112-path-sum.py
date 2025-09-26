# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        sumList = []
        
        if not root:
            return False

        def dfs(root, valSum):
            if not root.left and not root.right:
                sumList.append(valSum + root.val)
                return

            if root.left:
                dfs(root.left, root.val + valSum) 
            if root.right: 
                dfs(root.right, root.val + valSum) 
            
            return

        
        dfs(root, 0)

        if targetSum in sumList:
            return True
        else:
            return False
        