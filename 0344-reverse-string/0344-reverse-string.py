class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        if len(s) == 1:
            return s

        for i in range(1, len(s) // 2 + 1):
            temp = s[i - 1]
            s[i - 1] = s[-i]
            s[-i] = temp
