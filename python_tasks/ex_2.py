# Числа и кол-во их повторений

def count_occurrences(nums: list) -> dict:
    res = {}
    for num in nums:
        if num in res:
            res[num] += 1
        else:
            res[num] = 1

    return res