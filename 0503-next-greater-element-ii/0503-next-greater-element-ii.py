class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr= nums[:] + nums[:]
        ans = [-1]*len(nums)
        for i in range(len(nums)):
            for j in range(i, len(arr)):
                if nums[i]<arr[j]:
                    ans[i] = arr[j]
                    break
        return ans
        