class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort(reverse=True)
        
        result = 0

        for i in range(k):
            
            temp = happiness[i] - i

            if temp <= 0:
                break
                
            result += temp
        
        return result