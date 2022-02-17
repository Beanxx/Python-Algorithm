# 344. 문자열 뒤집기


# sol1) 투 포인터를 이용한 스왑
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        

# sol2) 파이썬다운 방식
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        