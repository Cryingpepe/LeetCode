class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        if len(s) - k + 1 < 2 ** k:
            return False
        
        result = {}
        
        for i in range(len(s) - k + 1):

            if s[i:i+k] not in result:
                result[s[i:i+k]] = 1
                
                if len(result) == 2 ** k:
                    return True
        
        return False