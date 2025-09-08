class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        pair = {')' : '(', '}' : '{', ']' : '['}

        for i in s:
            if i in pair.values():
                stack.append(i)
            else:
                if len(stack) == 0 or stack.pop() != pair[i]:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
