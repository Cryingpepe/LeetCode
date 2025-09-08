class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        isRoundedUp = False

        for i in range(len(digits) - 1, -1, -1):

            if not isRoundedUp:

                if digits[i] == 9:
                    digits[i] = 0
                    isRoundedUp = True
                else:
                    digits[i] = digits[i] + 1
                    break
            else:
                if digits[i] == 9:
                    digits[i] = 0
                    isRoundedUp = True
                else:
                    digits[i] = digits[i] + 1
                    isRoundedUp = False
                    break
        
        if isRoundedUp:
            return [1] + digits
        else:
            return digits





        