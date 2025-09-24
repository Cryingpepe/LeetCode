class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        queue = deque()
        result = 0

        for char in s:
            
            if char not in queue:
                queue.append(char)

            else:
                if len(queue) > result:
                    result = len(queue)

                for i in range(queue.index(char) + 1):
                    queue.popleft()
                    
        if len(queue) > result:
            result = len(queue)

        return result

            