# 125. 유효한 팰린드롬
# 팰린드롬: 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장

# sol1) 리스트로 변환
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():  # pop(0): 문자열 중 첫번째 문자, pop(): 문자열 중 마지막 문자
                return False
            
        return True



# sol2) 데크 자료형을 이용한 최적화
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()
            
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True


# sol3) 슬라이싱 사용
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        
        # 슬라이싱
        return s == s[::-1] # 문자열 뒤집기