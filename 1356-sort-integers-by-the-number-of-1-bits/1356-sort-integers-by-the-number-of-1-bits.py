class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        result =[]
        hashmap = defaultdict(list)

        for i in arr:
            count = bin(i).count('1')
            hashmap[count].append(i)

        for i in sorted(hashmap.keys()):
            for j in sorted(hashmap[i]):
                result.append(j)

        return result
