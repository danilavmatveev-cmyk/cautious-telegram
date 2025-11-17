from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

# Правильное использование:
solution = Solution()
result = solution.twoSum([3, 3], 6)
print(result)  # Вывод: [0, 1]