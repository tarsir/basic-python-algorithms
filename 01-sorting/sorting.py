"""
sorting.py: A basic sorting implementation in Python
"""

def bubble_sort(numbers):
    sorted_list = numbers[:]
    swap = True
    while swap:
        swap = False
        for index in range(len(sorted_list) - 1):
            left_num = sorted_list[index]
            right_num = sorted_list[index+1]
            if left_num > right_num:
                sorted_list[index+1] = left_num
                sorted_list[index] = right_num
                swap = True
    return sorted_list

def insertion_sort(numbers):
    sorted_list = []
    for num in numbers:
        is_max = True
        for index, target in enumerate(sorted_list):
            if num <= target:
                sorted_list = sorted_list[:index] + [num] + sorted_list[index:]
                is_max = False
                break
        if is_max:
            sorted_list = sorted_list + [num]
    return sorted_list

def merge_sort(numbers):
    length = len(numbers)
    if length == 0 or length == 1:
        return numbers
    else:
        splitting_index = length / 2
        left_list, right_list = merge_sort(
            numbers[:splitting_index],
            numbers[splitting_index:]
        )
        return _merge_lists(left_list, right_list)

def _merge_lists(left_list, right_list):
    left_ptr, right_ptr = 0, 0
    while left_ptr < len(left_list) and right_ptr < len(right_list):
        pass

unsorted_numbers = [9, 7, 5, 6, 1, 4, 2]
print (bubble_sort(unsorted_numbers))
print (insertion_sort(unsorted_numbers))
