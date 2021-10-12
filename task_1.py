""" Красильников Илья
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
end = False
file_strings = []

while not end:
    content = input("Введите текст  ")
    file_strings.append(content+'\n')
    if content == "":
        end = True


with open("text.txt", "a") as tx_file:
    tx_file.writelines(file_strings)
