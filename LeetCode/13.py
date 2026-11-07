class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        decode = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        result = 0
        for i, c in enumerate(s[:-1]):
            if decode[c] < decode[s[i+1]]:
                result -= decode[c]
            else:
                result += decode[c]
        result += decode[s[-1]]
        return result
