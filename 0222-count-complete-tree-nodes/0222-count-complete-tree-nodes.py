# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        result = 0

        while queue:
            node = queue.popleft()

            if node:
                
                result +=1
                queue.append(node.left)
                queue.append(node.right)

        return result