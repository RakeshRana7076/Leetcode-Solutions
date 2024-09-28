class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        word = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ': 
                length += 1
                word = True
            elif word: 
                break

        return length