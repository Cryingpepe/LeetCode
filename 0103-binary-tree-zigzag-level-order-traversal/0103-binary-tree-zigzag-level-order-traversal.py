# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        queue = deque()
        queue.append(root)
        zig = True

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
            
            if zig:
                result.append(level)
            else:
                result.append(level[::-1])
            
            zig = not zig
        
        return result