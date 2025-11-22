class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                dic = {}
                for k in range(j + 1, n):
                    if target - (nums[i] + nums[j] + nums[k]) in dic:
                        l = [
                            
                                target - (nums[i] + nums[j] + nums[k]),
                                nums[i],
                                nums[j],
                                nums[k]]
                        l.sort()
                        ans.add(tuple( l
                            
                        ))
                    else:
                        dic[nums[k]] = k
        return list(ans)
