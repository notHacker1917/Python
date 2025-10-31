class Solution(object):
    def romanToInt(self, s):
        total = 0
        prev_value = 0
        for ch in reversed(s):
            if ch == 'I':
                value = 1
            elif ch == 'V':
                value = 5
            elif ch == 'X':
                value = 10
            elif ch == 'L':
                value = 50
            elif ch == 'C':
                value = 100
            elif ch == 'D':
                value = 500
            elif ch == 'M':
                value = 1000
            else:
                value = 0  
            if value < prev_value:
                total = total - value
            else:
                total = total - value
            prev_value = value
        return total
