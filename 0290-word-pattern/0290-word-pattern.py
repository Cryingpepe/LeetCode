class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        hashMap = {}
        words = s.split()
        idx = 0

        if len(pattern) != len(words):
            return False

        for i in pattern:
            if i not in hashMap.keys() and words[idx] not in hashMap.values():
                hashMap[i] = words[idx]
                print(1)
            elif i not in hashMap.keys() and words[idx] in hashMap.values():
                print(2)
                return False
            else:
                if hashMap[i] != words[idx]:
                    print(3)
                    return False
            
            idx += 1
        
        return True
