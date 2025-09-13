# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

        stack = []

        def loop(root):
            if not root:
                return

            if root.left:
                if root.right:
                    stack.append(root.right)

                root.right = root.left
                root.left = None

            elif not root.right and stack:
                root.right = stack.pop()

            loop(root.right)

        loop(root)
                
        