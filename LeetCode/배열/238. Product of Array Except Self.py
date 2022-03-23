# 238. 자신을 제외한 배열의 곱

# sol1) 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
            # if input [1,2,3,4] -> p = 1, 1, 2, 6

        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums)-1, 0-1, -1):  # index: -3~0
            out[i] = out[i] * p
            p = p * nums[i]
            # p = 1, 4, 12, 24 => 24, 12, 4, 1
        return out  # 1x24, 1x12, 2x4, 6x1 => 24, 12, 8, 6
