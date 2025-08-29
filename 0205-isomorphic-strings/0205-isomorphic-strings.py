class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dictForS = OrderedDict()
        dictForT = OrderedDict()
        
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

        if dictForS.values() == dictForT.values():
            return True
        else:
            print(dictForS)
            print(dictForT)
            print(dictForS.values())
            print(dictForT.values())
            return False