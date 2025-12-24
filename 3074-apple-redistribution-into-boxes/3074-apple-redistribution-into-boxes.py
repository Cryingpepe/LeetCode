class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        count = 0
        weight = sum(apple)
        boxes = 0

        while boxes < weight:
            idx = capacity.index(max(capacity))
            boxes += capacity.pop(idx)
            count += 1

        return count