from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        lp = 1
        for i in range(len(ans)):
            ans[i] = lp
            lp *= nums[i]
        rp = 1
        for i in range(len(ans)-1, -1, -1):
            ans[i] *= rp
            rp *= nums[i]
        return ans