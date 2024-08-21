import sqlite3

db = sqlite3.connect('db.db')
sql = db.cursor()

def _create_bank_account_if_not_exists() -> None:
    """
    Создает аккаунт банка с N-ным кол-вом ресурса
    """
    setup1 = sql.execute(
        f"SELECT login FROM users WHERE login = 'bank' AND password = 'bank'"
    )
    sql.execute(setup1)
    setup2 = sql.fetchall()
    if setup2 == None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?) ", ('bank', 'bank', 'bank'))
        sql.execute(f"INSERT INTO diamond VALUES (?, ?)", ('bank', 0))
        sql.execute(f"INSERT INTO iron VALUES (?, ?)", ('bank', 10000))
        sql.execute(f"INSERT INTO gold VALUES (?, ?)", ('bank', 10000))
        sql.execute(f"INSERT INTO emerald VALUES (?, ?)", ('bank', 10000))
        sql.execute(f"INSERT INTO quartz VALUES (?, ?)", ('bank', 10000))
        sql.execute(f"INSERT INTO nezerite VALUES (?, ?)", ('bank', 10000))
        db.commit()
        db.commit()
        db.commit()
        db.commit()
        db.commit()
        db.commit()
    else:
        None
