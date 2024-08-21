from sqlite3 import Cursor


def _create_bank_account_if_not_exists():
    ...


def setup_db(cur: Cursor):
    """
    Создаёт таблицы пользователей и ресурсов, банковский аккаунт
    """

    # Создадим таблицу пользователей с автоинкрементирующимся (и уникальным) id
    # и уникальным логином
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL
    )""")

    # Создадим таблицу алмазов с автоинкрементирующимся (и уникальным) id
    # и полем user_id, которое является внешним ключом к users.id, то есть
    # каждая запись в diamond обязана быть привязанной к существующему
    # пользователю
    cur.execute("""CREATE TABLE IF NOT EXISTS diamond (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        count INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )""")

    _create_bank_account_if_not_exists()
