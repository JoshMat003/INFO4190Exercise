print("Input integers: ")

# Integer conversion and storage
nums = list(map(int, input().split()))
# Sorts the Numbers
nums.sort()

# Reverses the order
nums.reverse()

# Prints out the sorted inputed integers
print("Sorted Integers", nums)

# Caculates the average of the numbers
average = sum(nums)/ len(nums)

# Output
print("The Average of the inputted numbers is: ", average)
