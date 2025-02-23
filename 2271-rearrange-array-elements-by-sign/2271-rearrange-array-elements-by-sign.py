class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in range(len(nums)):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        idx1, idx2 =0, 0
        idx = 0
        while idx1<len(pos) and idx2<len(neg):
            nums[idx] = pos[idx1]
            idx+=1
            nums[idx] = neg[idx2]
            idx1+=1
            idx2+=1
            idx+=1
        while idx1<len(pos):
            nums[idx]=pos[idx1]
            idx+=1
            idx1+=1
        while idx2<len(neg):
            nums[idx] = neg[idx2]
            idx+=1
            idx2+=1
        return nums