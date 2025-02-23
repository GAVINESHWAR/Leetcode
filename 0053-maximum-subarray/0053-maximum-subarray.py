class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr>ans:
                ans = curr
            if curr<0:
                curr = 0
        return ans