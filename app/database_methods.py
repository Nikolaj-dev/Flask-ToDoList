import sqlite3


def add_notes(note_id, note_text):
    connection = sqlite3.connect('app/example.db')
    cursor = connection.cursor()
    cursor.execute(
        f"INSERT INTO note(note_id, text) VALUES ('{note_id}', '{note_text}')"
    )
    connection.commit()


def task_list(note_id):
    connection = sqlite3.connect('app/example.db')
    cursor = connection.cursor()
    res = cursor.execute(f"SELECT id, text FROM note WHERE note_id = {note_id}")
    result = res.fetchall()
    return result


def get_one_task(id_):
    connection = sqlite3.connect('app/example.db')
    cursor = connection.cursor()
    res = cursor.execute(f"SELECT text FROM note WHERE id = {id_}")
    result = res.fetchone()
    return result
