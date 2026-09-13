numbers = [10, 5, 20, 8, 15]

def second_largest(number_list):
    first_largest_num = number_list[0]
    second_largest_num = number_list[1]
    for x in number_list:
        if x > first_largest_num:
            second_largest_num = first_largest_num
            first_largest_num = x
    return second_largest_num

second = second_largest(numbers)
print(second)