import datetime


def append():
    note_title = input("Введите название заметки: ")
    note_text = input("Введите текст заметки: ")
    time = datetime.datetime.now().strftime("%A, %d %m %Y")
    data_note = note_title, note_text, time
    return data_note

