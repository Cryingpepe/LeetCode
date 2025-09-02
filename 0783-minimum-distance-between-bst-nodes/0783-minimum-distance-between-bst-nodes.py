# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        self.diff = 1000000
        self.preValue = None

        def DFS(root):
            if root:
                DFS(root.left)

                if self.preValue != None:
                    self.diff = min(self.diff, root.val - self.preValue)
                
                self.preValue = root.val
                DFS(root.right)
        
        DFS(root)

        return self.diff