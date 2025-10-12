class Solution:
    def candy(self, ratings: List[int]) -> int:

        if not ratings:
            return 0

        total = len(ratings)
        up = 0
        down = 0
        peak = 0

        for i in range(1, len(ratings)):

            if ratings[i] > ratings[i-1]:
                up += 1
                peak = up
                down = 0
                total += up
                
            elif ratings[i] == ratings[i-1]:
                up = 0
                down = 0
                peak = 0

            else:
                up = 0
                down += 1
                total += down - 1
                if peak < down:
                    total += 1
        
        return total





