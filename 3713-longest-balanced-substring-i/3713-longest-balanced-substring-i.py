class Solution:
    def longestBalanced(self, s: str) -> int:
        
        result = 0

        for i in range(len(s)):

            hashmap = {}

            for j in range(i, len(s)):

                hashmap[s[j]] = hashmap.get(s[j], 0) + 1 # 0 if there is no s[j], +1 if s[j] exists.

                freq = hashmap.values()

                if len(set(freq)) == 1: # if frequency of every chars in hashmap is equal,
                    result = max(result, j - i + 1)

        return result


