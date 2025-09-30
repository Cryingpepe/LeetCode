class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        maxLength = 0
        hashMap = {}

        for i in nums:

            if i in hashMap:
                continue
            
            if i - 1 not in hashMap and i + 1 not in hashMap:
                hashMap[i] = 1

                if hashMap[i] > maxLength:
                    maxLength = hashMap[i]

            elif i - 1 in hashMap and i + 1 not in hashMap:
                leftEndNum = i - hashMap[i - 1]

                hashMap[i] = hashMap[leftEndNum] + 1
                hashMap[leftEndNum] += 1

                if hashMap[leftEndNum] > maxLength:
                    maxLength = hashMap[leftEndNum]

            elif i - 1 not in hashMap and i + 1 in hashMap:
                rightEndNum = i + hashMap[i + 1]

                hashMap[i] = hashMap[rightEndNum] + 1
                hashMap[rightEndNum] += 1

                if hashMap[rightEndNum] > maxLength:
                    maxLength = hashMap[rightEndNum]

            else:
                rightEndNum = i + hashMap[i + 1]
                leftEndNum = i - hashMap[i - 1]

                temp = hashMap[rightEndNum]
                hashMap[rightEndNum] += hashMap[leftEndNum] + 1
                hashMap[leftEndNum] += temp + 1
                hashMap[i] = hashMap[rightEndNum]

                if hashMap[rightEndNum] > maxLength:
                    maxLength = hashMap[rightEndNum]
            
        return maxLength
            
