import sys

def insertion_sort(array):
	for index in range(1, len(array)):
		while 0 < index and array[index] < array[index -1]:
			array[index], array[index-1] = array[index-1], array[index]
			index -= 1
	return array


if __name__ == "__main__":
	if sys.version_info.major < 3:
		input_function = raw_input
	else:
		input_function = input
	user_input = input_function("Enter numbers seperated by comma : ")
	unsortedlist = [int(i) for i in user_input.split(',')]
	print insertion_sort(unsortedlist)