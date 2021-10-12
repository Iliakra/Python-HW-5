""" Красильников Илья
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open("txt_for_task_2.txt") as file_obj:
    content = file_obj.readlines()
    print(f"Количество строк в файле: {len(content)}")
    for index, el in enumerate(content):
        string_list = el.split()
        print(f"строка № {index+1} - количество слов {len(string_list)}")


