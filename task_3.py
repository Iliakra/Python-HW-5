""" Красильников Илья
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""

with open("txt_for_task_3.txt", encoding="utf-8") as file_obj:
    content = file_obj.readlines()
    salary = 0
    for el in content:
        string_list = el.split(" - ")
        if int(int(string_list[1])) < 20000:
            print(string_list[0])
        salary += int(string_list[1])
    print("Средняя величина дохода сотрудников - ", salary / len(content))
