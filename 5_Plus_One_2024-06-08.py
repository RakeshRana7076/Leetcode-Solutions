class Solution(object):
    def plusOne(self, digits):
        for i in reversed(range(len(digits))):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                return digits
        return [1] + digits


digits = [1, 3, 4]
sol = Solution()
print(sol.plusOne(digits))  

digits = [4,3,2,1]
print(sol.plusOne(digits)) 
digits=[9]
print(sol.plusOne(digits))