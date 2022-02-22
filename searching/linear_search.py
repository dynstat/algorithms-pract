# simple and recursive linear search in python

def linear_search(array: list, to_find: int):
    # sourcery skip: use-next,--> return next((index for (index, value) in enumerate(array) if value == to_find), -1)
    for (index, value) in enumerate(array):
        if value == to_find:
            return index
    return -1


if __name__ == "__main__":
    arr = [4, 6, 7, 8, 2, 9, 3, 0, ]
    to_find = int(input(f"Enter the number to find in the given array\n"))
    output = linear_search(arr, to_find)

    if output != -1:
        print(f"The item {to_find} was found at index = {output}\n")
    else:
        print(f"Your item {to_find} was not found in array {arr}")
