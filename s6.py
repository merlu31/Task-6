#You have been three lists. Your task is to find the duplicates in the three lists. Write a python program for the same. 
#You can use your own python lists?
def duplicate(input_list):
	new_dict, new_list = {}, []

	for i in input_list:
		if not i in new_dict:
			new_dict[i] = 1
		else:
			new_dict[i] += 1

	for key, values in new_dict.items():
		if values > 1:
			new_list.append(key)

	return new_list

if __name__ == '__main__':
	input_list1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
	print(duplicate(input_list1))
	input_list2 = [11, 22, 11, 22, 33, 44, 55, 11, 11, 22, 55, 66, 77, 88, 99, 99]
	print(duplicate(input_list2))
	input_list3 = [111, 222, 111, 222, 333, 444, 555, 111, 111, 222, 555, 666, 777, 888, 999, 999]
	print(duplicate(input_list3))