# simple and recursive linear search in python

def linear_search(array: list, to_find: int):
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
    recursive_linear_search(array, start_index+1, end_index-1, to_find)


if __name__ == "__main__":
    arr = [4, 6, 7, 8, 2, 9, 3, 0, ]
    to_find = int(input('Enter the number to find in the given array\n'))
    # output = linear_search(arr, to_find)
    output = recursive_linear_search(arr, 0, 5, to_find)

    if output != -1:
        print(f"The item {to_find} was found at index = {output}\n")
    else:
        print(f"Your item {to_find} was not found in array {arr}")
