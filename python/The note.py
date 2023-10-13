import json
import datetime


def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


notes = load_notes()


def save_notes(the_notes):
    with open('notes.json', 'w') as file:
        json.dump(the_notes, file, indent=4)


def add_note():
    title = input("Введите название заметки: ")
    message = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        'id': len(notes) + 1,
        'title': title,
        'message': message,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена.")


def delete_note():
    note_id = int(input("Введите id заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка не найдена.")


def edit_note():
    note_id = int(input("Введите id заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            new_title = input("Введите новое название заметки: ")
            if new_title == "":
                new_title == note['title']
            else:
                note['title'] = new_title
            new_message = input("Введите новый текст заметки: ")
            if new_message == "":
                new_message = note['message']
            else:
                note['message'] = new_message

            note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно изменена")
            return
    print("Заметка не найдена")


def print_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Название: {note['title']}")
        print(f"Текст: {note['message']}")
        print(f"Дата/Время создания или последнего изменения: {note['timestamp']}")
        print()


while True:
    print("Список возможных команд:")
    print("1 = Список заметок")
    print("2 = Добавить заметку")
    print("3 = Удалить заметку")
    print("4 = Изменить заметку")
    print("0 = Выйти")
    command = input("Введите цифру: ")

    if command == "1":
        print_notes()
    elif command == "2":
        add_note()
    elif command == "3":
        delete_note()
    elif command == "4":
        edit_note()
    elif command == "0":
        break
    else:
        print("Такой команды нет.")
