# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # def build(self, inorder, postorder):
    #     if inorder:
    #         idx = inorder.index(postorder.pop())
    #         root = TreeNode(inorder[idx])

    #         root.right = self.build(inorder[idx+1:], postorder)
    #         root.left = self.build(inorder[:idx], postorder)

    #         return root


    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """

        # return self.build(inorder, postorder)


        idx_map = {val: i for i, val in enumerate(inorder)}

        def build(in_left, in_right):
            if in_left > in_right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)

            idx = idx_map[root_val]

            root.right = build(idx + 1, in_right)
            root.left = build(in_left, idx - 1)

            return root

        return build(0, len(inorder) - 1)
