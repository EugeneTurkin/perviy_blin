import os
import sqlite3
from rot import rot13


class User():
    def __init__(self, email, password):
        self.email = email
        self.password = password


def logging_in():
    login = input('Enter your login: ')
    password = input('Enter your password: ')
    return User(login, password)


def manager(acc_info):
    user_input = input('Press "1" to add password. Press "2" to retrieve your password: ')
    if user_input == '1':
        user_email = input('Enter your e-mail: ')
        user_password = input('Enter your password: ')
        curs.execute("INSERT INTO userdat (owner_id, email, password) VALUES (:owner_id, :email, :password)",
        {'owner_id': curs.execute("SELECT id FROM accounts WHERE email=:email AND password=:password", {'email': acc_info.email, 'password': acc_info.password}).fetchone()[0],
        'email': user_email, 'password': user_password})
        print('Password is saved successfully')
    elif user_input == '2':
        user_email = input('Enter your e-mail: ')
        user_password = curs.execute("SELECT password FROM userdat WHERE owner_id=:owner_id AND userdat.email=:email",
        {'owner_id': curs.execute("SELECT id FROM accounts WHERE email=:email AND password=:password", {'email': acc_info.email, 'password': acc_info.password}).fetchone()[0],
        'email': user_email}).fetchone()
        user_password = user_password[0] if user_password is not None else ''
        print(f'Your password is: {rot13(user_password)}')


if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + '\\users.db'):
    conn = sqlite3.connect('users.db')
    curs = conn.cursor()
    print('Welcome back!')
    acc_info = logging_in()
    if curs.execute("SELECT email, password FROM accounts WHERE email=:email AND password=:password;", {'email': acc_info.email, 'password': acc_info.password}) is None:
        print('This account does not exist. Creating a new one.')
        curs.execute("INSERT INTO account (id, email, password) VALUES (:id, :email, :password)", {'id': curs.execute("SELECT (COUNT(*) + 1) FROM accounts;"), 'email': acc_info.email, 'password': acc_info.password})
else:
    print("Welcome to Gill Bates' Password Manager! Please, create an account by following the instructions.")
    acc_info = logging_in()
    conn = sqlite3.connect('users.db')
    curs = conn.cursor()
    curs.execute("""CREATE TABLE accounts (
                id          INTEGER     NOT_NULL,
                email       TEXT        NOT_NULL,
                password    TEXT        NOT_NULL
                )""")
    curs.execute("INSERT INTO accounts (id, email, password) VALUES (:id, :email, :password)", {'id': curs.execute("SELECT (COUNT(*) + 1) FROM accounts;").fetchone()[0], 'email': acc_info.email, 'password': acc_info.password})
    curs.execute("""CREATE TABLE userdat (
                owner_id    INTEGER     NOT_NULL,
                email       TEXT        NOT_NULL,
                password    TEXT        NOT_NULL
                )""")
    conn.commit()


manager(acc_info)
conn.close()




# файлы должны браться *относительно* места, где они лежат?
# хранение информации в БД
# 1) вынести создание таблиц в отдельный файл("установка")
# 2) гит (гитхаб ето другое) (системыа контроля версий)
# 3) 