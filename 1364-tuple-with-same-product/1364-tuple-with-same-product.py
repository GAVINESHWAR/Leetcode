class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_pairs = defaultdict(list)
        n = len(nums)
        count = 0

        # Build the product_pairs dictionary
        for i in range(n):
            for j in range(i+1, n):
                a, b = nums[i], nums[j]
                p = a * b
                product_pairs[p].append((a, b))

        # For each product, find the number of disjoint pairs
        for p, pairs in product_pairs.items():
            k = len(pairs)
            if k < 2:
                continue

            total_pairs = k * (k - 1) // 2

            # Count the occurrences of each element in the pairs
            element_counts = defaultdict(int)
            for a, b in pairs:
                element_counts[a] += 1
                element_counts[b] += 1

            # Calculate overlapping pairs
            overlapping_pairs = 0
            for count_element in element_counts.values():
                overlapping_pairs += count_element * (count_element - 1) // 2

            # Subtract overlapping pairs from total pairs to get non-overlapping pairs
            non_overlapping_pairs = total_pairs - overlapping_pairs

            # Each non-overlapping pair contributes 8 valid quadruplets
            count += non_overlapping_pairs * 8

        return count