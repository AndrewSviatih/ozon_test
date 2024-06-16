# Произведение всех ненулевых чисел

def product_of_nonzero_numbers(nums: list) -> int:
    product = 1

    for num in nums:
        if num != 0:
            product *= num

    return product