def lowest_word_len(arr_str):
    min_len = 0
    min_len = len(arr_str[0])
    for word in arr_str:
        min_len = min(min_len, len(word))

    return min_len


def lowest_match(arr_str):
    string = ''
    for i in range(lowest_word_len(arr_str)):
        for j in range(1, len(arr_str)):  # 1,2
            if arr_str[0][i] == arr_str[j][i]:
                if j == len(arr_str)-1:
                    string = string + arr_str[0][i]
            else:
                print(string)
                return string


if __name__ == "__main__":
    arr_str = ["flower", "flow", "flight"]
    lowest_match(arr_str)
