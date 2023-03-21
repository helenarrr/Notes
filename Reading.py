import csv


def read_note():
    with open("notes.csv", encoding="utf-8-sig") as n:
        n_reader = csv.reader(n, delimiter=";")
        for row in n_reader:
            print(row)
