class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        lmax = height[left]
        rmax = height[right]
        result = 0

        while left < right:
            
            if lmax < rmax:
                left += 1
                lmax = max(lmax, height[left])
                result += lmax - height[left]

            else:
                right -= 1
                rmax = max(rmax, height[right])
                result += rmax - height[right]
        
        return result