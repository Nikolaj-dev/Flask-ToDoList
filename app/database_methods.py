import sqlite3


def add_notes(note_id, task_text):
    connection = sqlite3.connect('app/example.db')
    cursor = connection.cursor()
    cursor.execute(
        f"INSERT INTO note(note_id, text) VALUES ('{note_id}', '{task_text}')"
    )
    connection.commit()


def task_list(note_id):
    connection = sqlite3.connect('app/example.db')
    cursor = connection.cursor()
    res = cursor.execute(f"SELECT * FROM note WHERE note_id = {note_id}")
    result = res.fetchall()
    return result

