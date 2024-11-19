class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        freq_map = {}
        
        for i in range(len(nums)):
            current_sum += nums[i]
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
            if i >= k:
                left_element = nums[i - k]
                current_sum -= left_element
                freq_map[left_element] -= 1
                if freq_map[left_element] == 0:
                    del freq_map[left_element]
            if i >= k - 1 and len(freq_map) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum
