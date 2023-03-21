import csv
from datetime import datetime


def edit_file():
    with open("notes.csv",  "r", encoding="utf-8-sig") as n:
        reader = csv.reader(n, delimiter=";")

        list_reader = list(reader)

        flag = input("Какую заметку вы хотите редактировать? Введите id заметки: ")

        for row in range(len(list_reader)):
            if flag == list_reader[row][0]:
                line = int(input("Что вы хотите изменить? Введите цифру: 1 - название; 2 - текст заметки: "))
                if line == 1:
                    list_reader[row][1] = input("Введите новое название заметки: ")
                if line == 2:
                    list_reader[row][2] = input("Введите новый текст заметки: ")
                list_reader[row][3] = datetime.now().strftime("%A, %d %m %Y")

    with open("notes.csv",  "w", encoding="utf-8-sig", newline='') as n:
        writer = csv.writer(n, delimiter=";")
        writer.writerows(list_reader)


