class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        diff = float(inf)
        result = []

        for i in range(1, len(arr)):
            current = arr[i] - arr[i - 1]

            if current < diff:
                diff = current
                result = [[arr[i - 1], arr[i]]]

            elif diff == current:
                result.append([arr[i - 1], arr[i]])

        return result