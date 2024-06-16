# Составить массив, где 1й элемент - разница между первым значением и последним
# 2й – разница между 2м и предпоследним и т.д.

def diff_btw_nums_to_centr(nums: list) -> list:
    res = []
    nums_len = len(nums)
    i = 0
    j = nums_len - 1

    while i <= j:
        res.append(nums[i] - nums[j])
        i += 1
        j -= 1
    
    return res