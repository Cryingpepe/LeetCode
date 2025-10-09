class Solution:
    def reverseWords(self, s: str) -> str:
        
        result = ""
        words = s.split()

        for i in words[::-1]:
            result += (i + " ")
        
        return result[:-1]

