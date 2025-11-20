print("Input integers: ")

nums = list(map(int, input().split()))

nums.sort()

nums.reverse()

print("Sorted Integers", nums)

average = sum(nums)/ len(nums)

print ("The Average of the inputted numbers is: ", average)