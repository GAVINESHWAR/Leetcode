class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums)-k+1):
            window = nums[i:i+k]
            max1 = max(window)
            c = 0
            for j in range(k-1):
                if window[j+1]-window[j]!=1:
                    c=1
                    break
            if c==0:
                ans.append(max1)
            else:
                ans.append(-1)
        return ans
        