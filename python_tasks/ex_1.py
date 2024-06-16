# Четные числа

def even_nums(nums: list) -> list:
    res = []
    for num in nums:
        if num % 2 == 0:
            res.append(num)
    
    return res