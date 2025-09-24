class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        if numerator == 0:
            return "0"

        if (numerator < 0) ^ (denominator < 0):
            result = "-"
        else:
            result = ""

        numerator = abs(numerator)
        denominator = abs(denominator)

        integer_part = numerator // denominator
        result = result + str(integer_part)

        numerator = numerator % denominator

        if numerator == 0:
            return result

        result = result + "."

        seen = {}
        while numerator != 0:
            if numerator in seen:
                start = seen[numerator]
                prefix = result[:start]
                repeating = result[start:]
                return prefix + "(" + repeating + ")"

            seen[numerator] = len(result)
            numerator = numerator * 10
            digit = numerator // denominator
            result = result + str(digit)
            numerator = numerator % denominator

        return result
