""" Красильников Илья
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

with open("txt_for_task_6.txt", encoding="utf-8") as file_obj:
    content = file_obj.readlines()
    my_dict = {el.split(": ")[0]: el.split(": ")[1] for el in content}
    for key, value in my_dict.items():
        hour_sum = 0
        value_list = value.split()
        for i in value_list:
            num = int(i.split("(")[0])
            hour_sum += num
        my_dict.update({key: hour_sum})
    print(my_dict)
