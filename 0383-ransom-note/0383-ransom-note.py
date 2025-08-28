class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        dictForChr = {}

        for i in magazine:
            if i not in dictForChr:
                dictForChr[i] = 1

            else:
                dictForChr[i] += 1

        try:
            for i in ransomNote:
                dictForChr[i] -= 1
        except:
            return False
        
        if min(dictForChr.values()) < 0:
            return False
        else:
            return True

            
             