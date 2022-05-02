import os
import sqlite3


class User():
    def __init__(self, email, password):
        self.email = email
        self.password = password


def owner_id(acc_info):
    owner_id = conn.execute(
        "SELECT id FROM accounts WHERE login = :login AND password = :password",
        {'login': acc_info.email, 'password': acc_info.password},
    ).fetchone()
    return owner_id[0]


def add_password(acc_info):
    user_email = input('Enter your e-mail: ')
    user_password = input('Enter your password: ')

    curs.execute(
        "INSERT INTO acc_data (owner_id, login, password) VALUES (:id, :login, :password)",
        {'id': owner_id(acc_info), 'login': user_email, 'password': user_password},
    )
    conn.commit()
    print('Password is saved successfully')


def retrieve_password(acc_info):
    user_email = input('Enter your e-mail: ')
    password = curs.execute(
        "SELECT password FROM acc_data WHERE login = :login AND owner_id = :id",
        {'login': user_email, 'id': owner_id(acc_info)},
    ).fetchone()
    if password is None:
        print('Password not found.')
    else:
        print('Your password is: ' + password[0])


def logging_in():
    login = input('Enter your login: ')
    password = input('Enter your password: ')

    accounts = curs.execute(
        "SELECT * FROM accounts WHERE login=:login AND password=:password",
        {'login': login, 'password': password},
    ).fetchall()

    if accounts == []:
        print('This account does not exist. Creating a new one.')
        curs.execute(
            "INSERT INTO accounts (login, password) VALUES (:login, :password)",
            {'login': login, 'password': password},
        )
        conn.commit()

    return User(login, password)


conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users', 'database.db'))
curs = conn.cursor()

acc_info = logging_in()
user_input = input('Press "1" to add password. Press "2" to retrieve your password: ')
if user_input == '1':
    add_password(acc_info)
elif user_input == '2':
    retrieve_password(acc_info)
