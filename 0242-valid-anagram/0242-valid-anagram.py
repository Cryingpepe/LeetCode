class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        hashMap = {}

        for i in s:
            if i not in hashMap.keys():
                hashMap[i] = 1
            else:
                hashMap[i] += 1

        for i in t:
            if i not in hashMap.keys():
                return False
            else:
                hashMap[i] -= 1

        for i in hashMap.values():
            if i != 0:
                return False
        
        return True
        
