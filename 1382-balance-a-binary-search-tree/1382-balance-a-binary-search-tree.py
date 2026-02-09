# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        nodes = []

        def inorder(root):

            if not root:
                return

            inorder(root.left)
            nodes.append(root)
            inorder(root.right)
        
        inorder(root)

        def buildTree(leftIdx, rightIdx):

            if leftIdx > rightIdx:
                return None
            
            mid = (leftIdx + rightIdx) // 2

            node = nodes[mid]

            node.left = buildTree(leftIdx, mid - 1)
            node.right = buildTree(mid + 1, rightIdx)

            return node

        return buildTree(0, len(nodes) - 1)