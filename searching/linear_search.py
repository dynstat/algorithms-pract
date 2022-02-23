# simple and recursive linear search in python

import sys


def linear_search(array: list[int], to_find: int):
    # sourcery skip: use-next,--> return next((index for (index, value) in enumerate(array) if value == to_find), -1)
    for (index, value) in enumerate(array):
        if value == to_find:
            return index
    return -1


def recursive_linear_search(array, start_index, end_index, to_find):
    if array[start_index] == to_find:
        return start_index
    if array[end_index] == to_find:
        return end_index
    if start_index > end_index:
        return -1
    # why not calling recursive function without return below ??
    return recursive_linear_search(array, start_index+1, end_index-1, to_find)


def double_linear_search(array: list[int], start_index, end_index, to_find):
    while start_index <= end_index:
        if array[start_index] == to_find:
            return start_index
        elif array[end_index] == to_find:
            return end_index
        else:
            start_index += 1
            end_index += 1
    return -1


def recursive_double_linear_search(array: list[int], start_index, end_index, to_find):
    if array[start_index] == to_find:
        return start_index
    if array[end_index] == to_find:
        return end_index
    if start_index > end_index:
        return -1
    return recursive_double_linear_search(array, start_index+1, end_index-1, to_find)


if __name__ == "__main__":
    arr = [4, 6, 7, 8, 2, 9, 3, 0, ]
    try:
        to_find = int(input('Enter the number to find in the given array\n'))
    except:
        print("invalid input")
        sys.exit(0)
    # output = linear_search(arr, to_find)
    # output = double_linear_search(arr, 0, 5, to_find)
    # output = recursive_linear_search(arr, 0, 5, to_find)
    output = recursive_double_linear_search(arr, 0, 5, to_find)

    if output != -1:
        print(f"The item {to_find} was found at index = {output}\n")
    else:
        print(f"Your item {to_find} was not found in array {arr}")
