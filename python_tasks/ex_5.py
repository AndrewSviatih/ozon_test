# Список разниц между соседними уникальными числами, 
# которые отсортированы по возрастанию

def decrease_unique_neighbors(nums: list) -> list:
    unique_nums = sorted(set(nums))
    res = []

    for i in (range(len(unique_nums) - 1)):
        res.append(unique_nums[i + 1] - unique_nums[i])

    return res