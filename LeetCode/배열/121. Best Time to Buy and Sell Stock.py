# 121. 주식을 사고팔기 가장 좋은 시점

# sol1) 브루트 포스로 계산
# Time Limit Exceeded!!
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 최댓값, 최솟값의 초깃값 지정
        profit = 0  # 최댓값 즉, 이익 (-sys.maxsize 로 지정하면 시스템의 최솟값으로 지정)
        min_price = sys.maxsize  # 최솟값을 시스템의 최댓값으로 지정해 바로 교체될 수 있도록.

        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)

        return profit


# sol2) 저점과 현재 값과의 차이 계산
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0  # 최댓값 즉, 이익
        min_price = sys.maxsize  # 최솟값을 시스템의 최댓값으로 지정해 바로 교체될 수 있도록.

        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
