class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        num = set(nums1)
        arr = set()

        for x in nums2:
            if x in num:
                arr.add(x)

        return list(arr)