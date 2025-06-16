class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        value = float('-inf')
        n = len(nums)
        mi = nums[0]
        c = 0
        for i in range(1, n):
            if nums[i]>mi:
                value = max(value, nums[i]-mi)
                c+=1
            mi = min(mi, nums[i])
        if c>0:
            return value
        return -1
        # for i in range(n):
        #     for j in range(i+1, n):
        #         value = max(value, nums[j]-nums[i])
        # return value
        