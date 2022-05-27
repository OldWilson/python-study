class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return s == ''

s = '{[]()[]}()'
solution = Solution()
print(solution.isValid(s))