import sys

def quick_sort(array):
	array_length = len(array)
	if array_length <= 1:
		return array
	else:
		pivot = array[0]
		greater = [element for element in array[1:] if element > pivot]
		lesser = [element for element in array[1:] if element <= pivot]
		return quick_sort(lesser) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
	if sys.version_info.major < 3:
		input_function = raw_input
	else:
		input_function = input
	user_input = input_function("Enter number seperated by comma : ")
	unsorted = [int(item) for item in user_input.split(',')]
	print quick_sort(unsorted)