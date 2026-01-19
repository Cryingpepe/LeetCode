"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        result = []
        
        def postOrder(root):

            if not root:
                return

            for node in root.children:
                postOrder(node)
                result.append(node.val)
        
        if not root:
            return []

        postOrder(root)
        result.append(root.val)
        
        return result