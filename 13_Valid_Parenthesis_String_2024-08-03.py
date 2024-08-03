class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min_left = max_left = 0
    
        for char in s:
            if char == '(':
                min_left += 1
                max_left += 1
            elif char == ')':
                min_left = max(min_left - 1, 0)
                max_left -= 1
                if max_left < 0:
                    return False
            elif char == '*':
                min_left = max(min_left - 1, 0)
                max_left += 1
        
        return min_left == 0