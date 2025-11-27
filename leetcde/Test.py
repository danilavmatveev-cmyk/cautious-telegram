class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quick_sort(left) + middle + quick_sort(right)
        if k == 1 or  k == len(nums):
            return sum(nums)
        n = len(nums) % k
        new_nums = quick_sort(nums)
        return sum(new_nums[n:])






