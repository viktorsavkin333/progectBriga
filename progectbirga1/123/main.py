import sqlite3

from utils import setup_db

con = sqlite3.connect('exchange_database.db')
cur = con.cursor()


def _add_diamond(user_id: int, cnt: int):
    """
    Создаёт запись в таблице diamond для пользователя user_id и возвращает id
    записи
    """

    cur.execute(
        f"INSERT INTO diamond (user_id, count) VALUES ('{user_id}', '{cnt}')"
    )
    con.commit()

    cur.execute(f"SELECT id FROM diamond WHERE user_id='{user_id}'")
    record_id: int = cur.fetchone()[0]

    return record_id
    
    


def add_user(login: str, password: str, email: str):
    """ Создаёт пользователя в таблице users и возвращает его id """

    cur.execute(
        "INSERT INTO users (login, password, email) " +
        f"VALUES ('{login}', '{password}', '{email}')"
    )

    con.commit()

    cur.execute(f"SELECT id FROM users WHERE login='{login}'")
    user_id: int = cur.fetchone()[0]

    _add_diamond(user_id, 0)

    return user_id


if __name__ == "__main__":
    setup_db(cur)

    # Создадим 10 новых пользователей с уникальными логинами
    for i in range(10):
        try:
            new_user_id = add_user(f"use{i}", f"pas{i}", f"ema{i}@mail.com")
            print(f"Id нового пользователя: {new_user_id}")
        except sqlite3.IntegrityError as e:
            print(f"Такой логин уже существует: use{i}")
