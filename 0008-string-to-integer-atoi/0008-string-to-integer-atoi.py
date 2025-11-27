class Solution:
    def myAtoi(self, s: str) -> int:
        
        if not s:
            return 0

        index = 0
        length = len(s)
        isNegative = False
        result = 0

        while index < length:
            if s[index] != ' ':
                break

            index += 1
        
        if index == length:
            return 0
        
        if s[index] == '-':
            isNegative = True
            index += 1

        elif s[index] == '+':
            index += 1
        
        while index < length:
            if s[index].isdigit():
                num = int(s[index])
                result = (result * 10) + num
            else:
                break

            if isNegative:
                if result * -1 <= -2 ** 31:
                    return -2 ** 31
            else:
                if result >= 2 ** 31 - 1:
                    return 2 ** 31 - 1
            
            index += 1
        
        return result if not isNegative else result * -1


