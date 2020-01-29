# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

nr_list = [10, 15, 3, 7]
result_list = []

k = int(input("Introduce k: "))

for a in nr_list:
    if k - a in nr_list:
        result_list.append(k - a)
        print(str(a) + " " + str(k - a))
