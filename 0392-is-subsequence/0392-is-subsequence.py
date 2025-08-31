class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        counter = 0
        
        if t == s:
            return True
        elif t == "":
            return False

        for i in s:
            if counter == len(t):
                return False
            elif i == t[counter]:
                counter += 1
                continue
            else:
                while i != t[counter]:
                    counter += 1
                    if counter == len(t):
                        return False
                counter += 1
        
        return True