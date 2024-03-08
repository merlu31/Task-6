#You have been given a python list[10,20,30,9] and a value of 59. Write a python program to find the triplet in the list 
#whose sum is equal to the given value?
def find_triplets(input_list, k):
	input_list.sort()
	result = []
	for i in range(len(input_list) - 2):
		left = i + 1
		right = len(input_list) - 1
		while left < right:
			if input_list[i] + input_list[left] + input_list[right] == k:
				result.append((input_list[i], input_list[left], input_list[right]))
				left += 1
				right -= 1
			elif input_list[i] + input_list[left] + input_list[right] < k:
				left += 1
			else:
				right -= 1
	return result
input_list = [10,20,30,9]
k = 59
print(find_triplets(input_list, k))
