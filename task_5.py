""" Красильников Илья
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from functools import reduce


def my_func(prev_el, el):
    return prev_el + el


user_numbers = input("Введите числа, разделенные пробелами   ")
content = []

with open("txt_for_task_5.txt", "w+") as file_obj:
    file_obj.write(user_numbers)
    file_obj.seek(0)
    content = file_obj.read()

content_list = content.split()
int_list = list(map(int, content_list))
result = reduce(my_func, int_list)

print(result)
