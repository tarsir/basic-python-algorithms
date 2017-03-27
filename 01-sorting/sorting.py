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
        splitting_index = int(length / 2)
        left_list, right_list = merge_sort(
            numbers[:splitting_index]
        ), merge_sort(
            numbers[splitting_index:]
        )
        return _merge_lists(left_list, right_list)

def _merge_lists(left_list, right_list):
    left_ptr, right_ptr = 0, 0
    combined_list = []
    while left_ptr < len(left_list) and right_ptr < len(right_list):
        if left_list[left_ptr] < right_list[right_ptr]:
            combined_list.append(left_list[left_ptr])
            left_ptr += 1
        else:
            combined_list.append(right_list[right_ptr])
            right_ptr += 1
    return combined_list + left_list[left_ptr:] + right_list[right_ptr:]

unsorted_numbers = [59, 98, 62, 94, 30, 91, 29, 6, 53, 70, 42, 83, 58, 12, 1, 11, 67, 25, 90, 7, 67, 49, 65, 60, 19, 16, 88, 13, 25, 85, 54, 76, 50, 43, 94, 83, 9, 98, 78, 72, 82, 10, 22, 75, 29, 40, 66, 77, 47, 92, 15, 61, 52, 1, 85, 82, 75, 2, 19, 32, 91, 16, 55, 5, 41, 15, 24, 2, 43,
49, 10, 90, 80, 11, 90, 25, 59, 37, 75, 33, 13, 48, 85, 84, 36, 22, 31, 83, 63, 96, 67, 89, 21, 100, 43, 94, 83, 7, 46, 65]
print (bubble_sort(unsorted_numbers))
print (insertion_sort(unsorted_numbers))
print (merge_sort(unsorted_numbers))
