from ex_1 import even_nums
from ex_2 import count_occurrences
from ex_3 import not_even_index_nums
from ex_4 import product_of_nonzero_numbers
from ex_5 import decrease_unique_neighbors
from ex_6 import reverse_nums
from ex_7 import average
from ex_8 import random_section
from ex_9 import diff_btw_nums_to_centr

nums = [0,1,2,0,5,10,13,4,3,3,13,1,22,2,8,10,0,8,5]

# 1. Четные числа
res = even_nums(nums)
print('1. Четные числа:')
print(res)

print()
# 2. Числа и кол-во их повторений
res = count_occurrences(nums)
print('2. Числа и кол-во их повторений:')
print(res)

print()
# 3. Числа на нечетных позициях
res = not_even_index_nums(nums)
print('3. Числа на нечетных позициях:')
print(res)

print()
# 4. Произведение всех ненулевых чисел
res = product_of_nonzero_numbers(nums)
print('4. Произведение всех ненулевых чисел')
print(res)

print()
# 5. Список разниц между соседними уникальными числами, 
# которые отсортированы по возрастанию
res = decrease_unique_neighbors(nums)
print('5. Список разниц между соседними уникальными числами,')
print('которые отсортированы по возрастанию:')
print(res)

print()
# 6. Перевернутый массив
res = reverse_nums(nums)
print('6. Перевернутый массив:')
print(res)

print()
# 7. Среднее значение
res = average(nums)
print('7. Среднее значение:')
print(round(res, 2))

print()
# 8. Произвольный отрезок значений в произвольном диапазоне
res = random_section(nums)
print('8. Произвольный отрезок значений в произвольном диапазоне:')
print(res)

print()
# 9. Составить массив, где 1й элемент - разница между первым значением и последним, 
# 2й – разница между 2м и предпоследним и т.д.
res = diff_btw_nums_to_centr(nums)
print('9. Составить массив,')
print('где 1й элемент - разница между первым значением и последним,')
print('2й – разница между 2м и предпоследним и т.д.')
print(res)