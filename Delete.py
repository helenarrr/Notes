import csv


def delete_file():
    with open("notes.csv", "r", encoding="utf-8-sig") as n:
        reader = csv.reader(n, delimiter=";")

        list_reader = list(reader)

        for index, row in enumerate(list_reader):
            print(index, row)

        flag = int(input("Какую заметку вы хотите удалить? Введите номер строки: "))
        del list_reader[flag]

    with open("notes.csv", "w", encoding="utf-8-sig", newline='') as n:
        writer = csv.writer(n, delimiter=";")
        writer.writerows(list_reader)
