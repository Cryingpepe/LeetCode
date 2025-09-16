class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)
        
        for i in strs:
            count = [0] * 26

            for char in i:
                count[ord(char) - ord("a")] += 1
            result[tuple(count)].append(i)
        
        return list(result.values())
            
