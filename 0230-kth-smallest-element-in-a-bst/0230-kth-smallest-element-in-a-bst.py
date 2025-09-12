# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
            

    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.k = k
        self.result = None

        def inorder(root):

            if root:
                inorder(root.left)
                
                self.k -= 1
                
                if self.k == 0:
                    self.result = root.val
                    return 
                
                inorder(root.right)

        inorder(root)

        return self.result
        