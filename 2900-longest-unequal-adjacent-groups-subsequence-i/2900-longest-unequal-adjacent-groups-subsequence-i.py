class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        result = []
        order = -1
        
        for i in range(len(groups)):
            
            if groups[i] != order:
                order = groups[i]
                result.append(words[i])

        return result