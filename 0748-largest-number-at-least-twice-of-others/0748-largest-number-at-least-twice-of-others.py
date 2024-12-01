class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi = max(nums)
        for i in range(len(nums)):
            if nums[i]!=maxi:
                if maxi<2 * nums[i]:
                    return -1
        return nums.index(maxi)