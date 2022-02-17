# 819. 가장 흔한 단어

# sol1) List Comprehension, Counter 객체 사용
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 단어 문자가 아닌 모든 문자를 공백으로 치환
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)  # ^: not, \w: 단어 문자
                .lower().split()
                    if word not in banned]
        
        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]