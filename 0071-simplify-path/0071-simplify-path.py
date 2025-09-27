class Solution:
    def simplifyPath(self, path: str) -> str:
        
        result = ""
        queue = deque()

        temp = path.split("/")

        for i in temp:
            if i == "..":
                if not queue:
                    continue
                queue.pop()

            elif i == ".":
                continue

            elif i:
                queue.append(i)
        
        for i in queue:
            result += "/" + i
        
        if not result:
            return "/"

        return result