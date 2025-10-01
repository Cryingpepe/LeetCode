class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]

        for j in range(len(strs[0])):
            char = strs[0][j]
            

            for i in range(1, len(strs)):
                if j == len(strs[i]) or strs[i][j] != char:
                    return strs[0][0:j]
        
        return strs[0]


        
