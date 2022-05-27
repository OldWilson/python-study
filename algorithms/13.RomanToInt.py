class Solution:
    def romanToInt(self, s: str) -> int:
        strMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and strMap[s[i]] < strMap[s[i + 1]]:
                result -= strMap[s[i]]
            else:
                result += strMap[s[i]]
        return result
