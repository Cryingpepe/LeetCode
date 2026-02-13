class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        sign = (dividend < 0) ^ (divisor < 0)

        print (sign)

        if sign:
            result = abs(dividend) // abs(divisor) * -1
        else:
            result = dividend // divisor

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result