# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def build(self, preorder, inorder):
        if inorder:
            idx = inorder.index(preorder.popleft())
            root = TreeNode(inorder[idx])

            root.left = self.build(preorder, inorder[:idx])
            root.right = self.build(preorder, inorder[idx+1:])

            return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        preorder = deque(preorder)

        return self.build(preorder, inorder)



        
        