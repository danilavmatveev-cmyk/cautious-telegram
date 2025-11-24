def findFinalValue(nums: List[int], original: int) -> int:
   cache = {}
   cache[original] = [x for x in range(original)]
   n = len(nums)
   if original not in nums:
      return original
   for i in range(n):

      if nums[i] not in cache[original]:
         if nums[i] == original:
            original = original * 2
