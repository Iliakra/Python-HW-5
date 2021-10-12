""" Красильников Илья
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

content = []

with open("txt_for_task_7.txt", encoding="utf-8") as file_obj:
    content = file_obj.readlines()

result_list = []
profit_dict = {el.split()[0]: int(el.split()[2])-int(el.split()[3]) for el in content if int(el.split()[2]) > int(el.split()[3])}
average_profit_dict = {"average_profit": sum(profit_dict.values()) / len(profit_dict.values())}
loss = {el.split()[0]: int(el.split()[2])-int(el.split()[3]) for el in content if int(el.split()[2]) <= int(el.split()[3])}
profit_dict.update(loss)
result_list.append(profit_dict)
result_list.append(average_profit_dict)
print(result_list)

with open("json_task_7.json", "w", encoding="utf-8") as write_file:
    json.dump(result_list, write_file)
