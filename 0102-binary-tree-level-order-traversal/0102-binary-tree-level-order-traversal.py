# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []

        if not root:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            
            level = []
            levelLength = len(queue)

            for _ in range(levelLength):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                level.append(node.val)
            
            result.append(level)
        
        return result
                


        