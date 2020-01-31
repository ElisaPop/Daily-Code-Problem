# Given an array of integers, return a new array such that each element at index i of the new array is the product
# of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
# [3, 2, 1], the expected output would be [2, 3, 6].

nr_list = [1, 2, 3, 4, 5]
product_list = nr_list.copy()
product = 1
length_list = len(nr_list)-1

for i in nr_list:
    product = product * i

for i in range(len(nr_list)):
    product_list[i] = product/nr_list[i]

print("Result with division: ")
print(product_list)

# Follow-up: what if you can't use division?

left_product = nr_list.copy()
right_product = nr_list.copy()
product1 = 1
product2 = 1

for i in range(len(nr_list)):
    product1 = product1 * nr_list[i]
    product2 = product2 * nr_list[i * -1 - 1]

    left_product[i] = product1
    right_product[i * -1 - 1] = product2

for i in range(len(product_list)):
    if i == 0:
        product_list[i] = right_product[i+1]
    elif i == len(product_list)-1:
        product_list[i] = left_product[i-1]
    else:
        product_list[i] = left_product[i-1] * right_product[i+1]

print("Result without division: ")
print(product_list)
