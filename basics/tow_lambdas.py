my_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(num):
    return num % 2 == 0


even_nums = filter(is_even, my_ints)
print(list(even_nums))

# using lambda
# transform above method to lambda

even_nums_2 = filter(lambda num: num % 2 == 0, my_ints)
print(list(even_nums_2))
