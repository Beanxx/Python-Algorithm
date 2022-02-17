# 49. 그룹 애너그램
# 애너그램: 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것

# sol1) 정렬하여 딕셔너리에 추가
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # error 방지를 위해 defaultdict()으로 선언하여 항상 디폴트 값 생성
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())