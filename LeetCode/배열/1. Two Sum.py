# 1. 두 수의 합

# sol1) 브루트 포스로 계산
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# sol2) in을 이용한 탐색
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return nums.index(n), nums[i+1:].index(complement)+(i+1)


# sol3) 첫 번째 수를 뺀 결과 키 조회
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # target에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return nums.index(num), nums_map[target-num]


# sol4) 조회 구조 개선
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 for문으로 통합
        for i, num in enumerate(nums):
            if target-num in nums_map:
                return [nums_map[target-num], i]  # return (value, index)
            nums_map[num] = i


# sol5) 투 포인터 이용
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort() <- 정렬 로직 추가 but, index가 엉망이 되어서 문제를 풀 수 없음.
        left, right = 0, len(nums)-1
        while not left == right:
            # 합이 target보다 크면 오른쪽 포인터를 왼쪽으로 <-
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 target보다 작으면 왼쪽 포인터를 오른쪽으로 ->
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return left, right


# sol6) 고(Go) 구현
func twoSum(nums[]int, target int)[]int {
    numsMap := make(map[int]int)

    // 키와 값을 바꿔서 딕셔너리로 저장
    for i, num := range nums {
        numsMap[num] = i
    }

    // 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num := range nums {
        if j, ok := numsMap[target-num]; ok & & i != j {
            return []int{i, j}
        }
    }

    return []int{}
}
