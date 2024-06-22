class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char = set()
        j = 0
        length = 0
        for i in range(len(s)):
            while s[i] in char:
                char.remove(s[j])
                j += 1
            char.add(s[i])
            length = max(length, i - j + 1)
        return length

solution = Solution()