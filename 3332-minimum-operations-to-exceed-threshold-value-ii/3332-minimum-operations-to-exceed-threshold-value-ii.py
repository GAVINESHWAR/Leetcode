class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operation = 0
        n = len(nums)
        heapq.heapify(nums)
        for i in range(n-1):
            if len(nums)>=2:
                x = heapq.heappop(nums)
                y = heapq.heappop(nums)
            if x<k or y<k:
                req = min(x, y)*2 + max(x, y)
                operation += 1
                heapq.heappush(nums,req)
            else:
                return operation
        return operation
