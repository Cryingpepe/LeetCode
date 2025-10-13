class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        def isAnagram(a, b):

            if len(a) != len(b):
                return False

            cnt = collections.Counter(a)

            for c in b:
                cnt[c] -= 1

                if cnt[c] < 0:
                    return False

            return True

        result = []

        for w in words:

            if not result:
                result.append(w)
            else:
                if not isAnagram(result[-1], w):
                    result.append(w)

        return result