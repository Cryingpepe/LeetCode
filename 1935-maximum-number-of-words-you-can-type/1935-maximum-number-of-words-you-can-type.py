class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """

        words = text.split()
        broken = set(brokenLetters)
        count = 0

        for i in words:
            notBroken = True

            for j in i:
                if j in broken:
                    notBroken = False
                    break
                    
            if notBroken:
                count += 1

        return count

        # words = text.split()
        # broken = set(brokenLetters)
        # count = 0

        # for i in words:
        #     if all(ch not in broken for ch in i):
        #         count += 1

        # return count