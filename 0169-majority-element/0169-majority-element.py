class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if i==0:
                element = nums[i]
                count+=1
            elif element == nums[i]: 
                count+=1
            elif element != nums[i] and count>0:
                count-=1
            elif element != nums[i] and count==0:
                element=nums[i]
                count+=1
        return element 