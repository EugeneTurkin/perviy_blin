import os
import sqlite3


conn = sqlite3.connect(os.path.dirname(os.path.abspath(__file__)) + '\\users\\database.db')
curs = conn.cursor()


def id_tech():
    return curs.execute("SELECT COUNT(*) FROM id_tech").fetchone()[0]


class User():
    def __init__(self, email, password):
        self.email = email
        self.password = password


def logging_in():
    login = input('Enter your login: ')
    password = input('Enter your password: ')
    if curs.execute("SELECT * FROM accounts WHERE email=:email AND password=:password", {'email': login, 'password': password}).fetchall is []:
        curs.execute("INSERT INTO accounts (id, email, password) VALUES (:id, :email, :password)", {'id': id_tech, 'email': login, 'password': password})
        conn.commit()
        print('This account does not exist. A new one was created.')
    return User(login, password)


def owner(acc_info):
    return curs.execute("SELECT id FROM accounts WHERE email=:email AND password=:password", {'email': acc_info.email, 'password': acc_info.password}).fetchone()[0]


def add_password(acc_info):
    user_email = input('Enter your e-mail: ')
    user_password = input('Enter your password: ')
    curs.execute("INSERT INTO acc_data (owner_id, email, password) VALUES (:id, :email, :password)", {'id': owner(acc_info), 'email': user_email, 'password': user_password})
    conn.commit()
    print('Password is saved successfully')


def retrieve_password(acc_info):
    user_email = input('Enter your e-mail: ')
    return curs.execute("SELECT acc_data.password FROM accounts, acc_data WHERE accounts.id = acc_data.owner_id AND acc_data.email=:email", {'email': user_email}).fetchone()[0]


def manager(acc_info):
    user_input = input('Press "1" to add password. Press "2" to retrieve your password: ')
    if user_input == '1':
        add_password(acc_info)
    elif user_input == '2':
        retrieve_password(acc_info)


if id_tech == 1:
    print("Welcome to Gill Bates' Password Manager! Please, create an account by following the instructions.")
    acc_info = logging_in()
else:
    print('Welcome back!')
    acc_info = logging_in()


manager(acc_info)