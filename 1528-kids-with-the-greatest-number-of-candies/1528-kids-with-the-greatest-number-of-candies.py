class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        result = [False]*len(candies)   
        for i in range(len(candies)):
            curr = extraCandies + candies[i]
            if curr>=maximum:
                result[i] = True
        return result