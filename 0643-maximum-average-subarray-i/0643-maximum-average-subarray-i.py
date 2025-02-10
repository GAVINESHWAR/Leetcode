class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sliding = nums[:k]
        sum1 = sum(sliding)
        curr = sum1
        for i in range(n-k):
            curr += nums[i+k]
            curr -= nums[i]
            sum1 = max(sum1, curr)
        return round(sum1/k, 5)


