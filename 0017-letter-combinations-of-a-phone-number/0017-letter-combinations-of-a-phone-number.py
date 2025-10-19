class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        result = []

        digitLetters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(idx, comb):
            if idx == len(digits):
                result.append(comb[:])
                return
            
            for letter in digitLetters[digits[idx]]:
                backtrack(idx + 1, comb + letter)

        backtrack(0, "")

        return result