# Числа на нечетных позициях

def not_even_index_nums(nums: list) -> list:
    res = []

    for i in range(len(nums)):
        if i % 2 != 0:
            res.append(nums[i])

    return res