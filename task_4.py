""" Красильников Илья
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

num_string_ru = ["Один", "Два", "Три", "Четыре"]
content = []
new_content = []
with open("txt_for_task_4.txt", encoding="utf-8") as file_for_read:
    content = file_for_read.readlines()

for index, el in enumerate(content):
    el_list = el.split(" - ")
    el_list[0] = num_string_ru[index]
    new_el = " - ".join(el_list)
    new_content.append(new_el)

with open("NEW_txt_for_task_4.txt", "w", encoding="utf-8") as file_for_write:
    file_for_write.writelines(new_content)
