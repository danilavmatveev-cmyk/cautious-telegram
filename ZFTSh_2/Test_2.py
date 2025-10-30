def sum_index(arr):
   if not arr:
       return 0

   return 1 + sum_index(arr[1:])

print(sum_index([1,2,3,4,6]))
