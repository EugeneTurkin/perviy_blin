import os
import sqlite3


os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users'))
conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users', 'database.db'))
curs = conn.cursor()

curs.execute("""CREATE TABLE accounts (
                id          INTEGER     PRIMARY KEY AUTOINCREMENT,
                login       TEXT        NOT_NULL,
                password    TEXT        NOT_NULL
                )""")

curs.execute("""CREATE TABLE acc_data (
                owner_id    INTEGER     NOT_NULL,
                login       TEXT        NOT_NULL,
                password    TEXT        NOT_NULL
                )""")
conn.commit()
