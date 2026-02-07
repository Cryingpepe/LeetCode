class Solution:
    def minimumDeletions(self, s: str) -> int:

        result = 0
        count = 0

        for i in s:
            if i == 'b':
                count += 1

            elif count:
                result += 1
                count -= 1
        
        return result