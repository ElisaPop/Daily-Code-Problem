# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

input_list = [3, 4, -1, 1]


def get_positives(input_list):
    i = 0
    j = len(input_list) - 1

    while i < j:
        if input_list[i] > 0 >= input_list[j]:
            input_list[i], input_list[j] = input_list[j], input_list[i]
            i += 1
            j -= 1
        elif input_list[i] > 0:
            j -= 1
        else:
            i += 1

    pivot = i if input_list[i] > 0 else i + 1
    return input_list[pivot:]


input_list = get_positives(input_list)
length = len(input_list)

if not input_list:
    print('1')

if max(input_list) == len(input_list):
    print(max(input_list) + 1)

for num in input_list:
    current_num = abs(num)
    if (current_num -1) < length:
        input_list[current_num - 1] *= -1

for i,num in enumerate(input_list):
    if num > 0:
        print(i + 1)