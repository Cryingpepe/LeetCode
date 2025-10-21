class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        comb = []

        def backtrack(num, numSum):
            if numSum == target:
                result.append(comb[:])
                return
            elif numSum > target:
                return
            
            
            for i in range(num, len(candidates)):
                comb.append(candidates[i])
                backtrack(i, numSum + candidates[i])
                comb.pop()

        backtrack(0, 0)
        
        return result