
def num_index(input_arr):
    arr = input_arr
    sorted_arr = sorted(arr)
    return '{} is the number that fits between {} and {} and ' \
           'the index of {} in the input array is {}.'.format(sorted_arr[1], sorted_arr[0], sorted_arr[-1], sorted_arr[1], input_arr.index(sorted_arr[1]))


if __name__ == '__main__':
    print(num_index([2, 3, 1]))
    print(num_index([5, 10, 14]))
    print(num_index([8, 21, 15]))
