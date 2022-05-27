class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xStr = str(x)
        length = len(xStr)
        left = 0
        right = length - 1
        while left < right:
            if xStr[left] != xStr[right]:
                return False
            left+=1
            right-=1
        return True


    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        xStr = str(x)
        newStr = xStr[::-1]
        return xStr == newStr

    def isPalindrome3(self, x: int) -> bool:
        if x < 0:
            return False
        xStr = str(x)
        # newStr = ''.join(list(reversed(xStr)))
        newStr = "".join(list(xStr).reverse())
        return xStr == newStr

x = 121
solution = Solution()
print(solution.isPalindrome2(x))
        