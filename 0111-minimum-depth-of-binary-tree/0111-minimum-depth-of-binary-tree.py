# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        queue = deque([root])
        result = 0

        while queue:
            levelLength = len(queue)
            result += 1

            for _ in range(levelLength):
                node = queue.popleft()

                if not node.left and not node.right:
                    return result

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

        
