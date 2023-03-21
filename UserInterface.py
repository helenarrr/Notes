from Adding import append
from Delete import delete_file
from Editing import edit_file
from ReadOne import select_reading
from Reading import read_note
from Saving import save_file
from Sorting import sort_file

# Приложение должно уметь сохранять данные
# в файл, уметь читать данные из файла, делать выборку по дате, выводить на
# экран выбранную запись, выводить на экран весь список записок, добавлять
# записку, редактировать ее и удалять.

text = "Выберите одно из следующих действий и нажмите соответствующую цифру:\n[1] - записать заметку в формате csv \n[2] - прочитать cписок всех заметок\n[3] - редактировать заметку\n[4] - удалить заметку\n[5] - вывести все заметки за определенную дату\n[6] - вывести заметку по номеру ID\nДля выхода нажмите [0]"


def menu():
    while True:
        print(text)
        flag = int(input())
        if flag == 1:
            save_file(append())
        elif flag == 2:
            read_note()
        elif flag == 3:
            edit_file()
        elif flag == 4:
            delete_file()
        elif flag == 5:
            sort_file()
        elif flag == 6:
            select_reading()
        elif flag == 0:
            break
        else:
            print("Упс, вы ввели что-то не то ... ")


