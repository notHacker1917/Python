class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        rev = ""
        for ch in s:
            rev = ch + rev  
        return s == rev  
