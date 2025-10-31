class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        result = []
        for i in dic:
            if dic[i] == 2:
                result.append(i)
        return result