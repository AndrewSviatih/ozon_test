# 7. Среднее значение

def average(nums: list) -> float:
    # здесь можно сделать average = sum(nums) / len(nums)
    # но я так понимаю, нужно посмотреть,
    # как я сделаю алгоритмически

    total = 0
    count = 0

    for num in nums:
        total += num
        count += 1

    average: float = total / count if count != 0 else 0

    return average