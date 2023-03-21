import csv


def save_file(data_note):
    with open('notes.csv', mode="a", encoding="utf-8-sig") as n:
        id_note = str(hash(data_note[1]))
        file_writer = csv.writer(n, delimiter=";", lineterminator="\r")
        file_writer.writerow([id_note[1:3], data_note[0], data_note[1], data_note[2]])


