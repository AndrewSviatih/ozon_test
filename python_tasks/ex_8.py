# 8. Произвольный отрезок значений в произвольном диапазоне
import random
def random_section(nums: list) -> list:

    nums_len = len(nums)
    min_index = random.randint(0, nums_len - 1)
    max_index = random.randint(min_index + 1, nums_len)

    res = nums[min_index:max_index]

    return res