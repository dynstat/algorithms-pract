''' BIT MASKING uses a mask like "00010000" and use it with other number while performing some logical operations to
    set 5th bit from the right.
'''


# Setting a bit
def set_bit(position, bin_value):
    mask = 1 << position  # "Left shift operator"
    result = bin_value | mask  # OR operator sets the bit at particular location"
    return result


if __name__ == "__main__":
    given_binValue = 0000000
    output = set_bit(5, given_binValue)
    print(output)
