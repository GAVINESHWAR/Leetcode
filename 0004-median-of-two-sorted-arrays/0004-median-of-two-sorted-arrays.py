class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []

        i, j = 0, 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                ans.append(nums1[i])
                i+=1
            else:
                ans.append(nums2[j])
                j+=1
        while i<len(nums1):
            ans.append(nums1[i])
            i+=1
        while j<len(nums2):
            ans.append(nums2[j])
            j+=1
        n= len(ans)
        if n%2==1:
            return float(ans[n//2])
        return float((ans[n//2] + ans[(n//2)-1])/2)
