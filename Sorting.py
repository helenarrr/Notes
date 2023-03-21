import csv


def sort_file():
    with open("notes.csv",  "r", encoding="utf-8-sig") as n:
        reader = csv.reader(n, delimiter=";")

        list_reader = list(reader)

        flag = input("Введите число, месяц и год через пробел (цифрами): ").split()

        for row in range(len(list_reader)):
            sort_date = list_reader[row][3][0:].split()
            num_list = []
            for word in sort_date:
                if word.isnumeric():
                    num_list.append(word)
            if flag == num_list:
                print(list_reader[row])










