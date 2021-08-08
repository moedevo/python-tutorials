#A Program to count the number 4 in a given list.

def fourcount(nums):
  count = 0
  for num in nums:
    if num == 4:
      count = count + 1
  return count
print(fourcount([1,2,4,5,4,5,5,4,4,4,4,4,4,4,4,4,44,4,4,5]))