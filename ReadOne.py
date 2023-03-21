import csv


def select_reading():
    with open("notes.csv", encoding="utf-8-sig") as n:
        reader = csv.reader(n, delimiter=";")

        list_reader = list(reader)

        flag = input("Какую заметку вы хотите посмотреть? Введите id заметки: ")

        for row in range(len(list_reader)):
            if flag == list_reader[row][0]:
                print(list_reader[row])
