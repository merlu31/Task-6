#Given a list[4,2,-3,6] write a python to find if there is a sub-list with sum equal to zero?
def subArrayExists(arr, n):
	for i in range(n):
		# Starting point of the subarray and
		# sum is initialized with the first element of subarray
		sum = arr[i]
		if sum == 0:
			return True
		for j in range(i + 1, n):
			# We are finding the sum till the jth index
			# starting from the ith index
			sum += arr[j]
			if sum == 0:
				return True
	return False
if __name__ == "__main__":
	arr = [4,2,-3,6]
	N = len(arr)

	# Function call
	if subArrayExists(arr, N):
		print("Found a subarray with 0 sum")
	else:
		print("No Such Sub Array Exists!")
