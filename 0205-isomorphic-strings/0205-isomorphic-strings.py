class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        dictForS = {}
        dictForT = {}
        
        for i, char in enumerate(s):
            if char not in dictForS:
                dictForS[char] = [i]
            else:
                dictForS[char].append(i)
        
        for i, char in enumerate(t):
            if char not in dictForT:
                dictForT[char] = [i]
            else:
                dictForT[char].append(i)

        for i in range(len(s)):
            if dictForS[s[i]] != dictForT[t[i]]:
                return False
        
        return True