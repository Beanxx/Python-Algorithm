# 42. 빗물 트래핑

# sol1) 투 포인터를 최대로 이동
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(
                height[right], right_max)

            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume


# sol2) 스택 쌓기
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0  # 채워지는 물 눞이

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            # stack[-1]: 스택에서 원소를 제거하지 않고 가져오기만 할 때 사용
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume
