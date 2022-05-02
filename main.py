import os
import sqlite3
# import password_manager


class User():
    def __init__(self, email, password):
        self.email = email
        self.password = password


def owner_id(acc_info):
    if conn.execute("SELECT id FROM accounts WHERE login = :login AND password = :password", {'login': acc_info.email, 'password': acc_info.password}).fetchall() == []:
        return None
    else:
        return curs.execute("SELECT id FROM accounts WHERE login = :login AND password = :password", {'login': acc_info.email, 'password': acc_info.password}).fetchall()[0][0]


def add_password(acc_info):
    user_email = input('Enter your e-mail: ')
    user_password = input('Enter your password: ')

    curs.execute("INSERT INTO acc_data (owner_id, login, password) VALUES (:id, :login, :password)", {'id': owner_id(acc_info), 'login': user_email, 'password': user_password})
    conn.commit()
    print('Password is saved successfully')


def retrieve_password(acc_info):
    user_email = input('Enter your e-mail: ')
    print('Your password is: ' + curs.execute("SELECT password FROM acc_data WHERE login = :login AND owner_id = :id", {'login': user_email, 'id': owner_id(acc_info)}).fetchone()[0])


def logging_in():
    login = input('Enter your login: ')
    password = input('Enter your password: ')
    
    if curs.execute("SELECT * FROM accounts WHERE login=:login AND password=:password", {'login': login, 'password': password}).fetchall() == []:
        print('This account does not exist. Creating a new one.')
        curs.execute("INSERT INTO accounts (id, login, password) VALUES (:id, :login, :password)", {'id': id_tech(), 'login': login, 'password': password})
        conn.commit()
    
    return User(login, password)

def id_tech():
    return curs.execute("SELECT * FROM id_tech").fetchone()[0]


if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + '\\users'):
    print('Welcome back!')

    conn = sqlite3.connect(os.path.dirname(os.path.abspath(__file__)) + '\\users\\database.db')
    curs = conn.cursor()

    acc_info = logging_in()
else:
    print("Welcome to Gill Bates' Password Manager! Please, create an account by following the instructions.")
    
    os.makedirs(os.path.dirname(os.path.abspath(__file__)) + '\\users')
    conn = sqlite3.connect(os.path.dirname(os.path.abspath(__file__)) + '\\users\\database.db')
    curs = conn.cursor()
    
    curs.execute("""CREATE TABLE accounts (
                    id          INTEGER     NOT_NULL,
                    login       TEXT        NOT_NULL,
                    password    TEXT        NOT_NULL
                    )""")
    
    curs.execute("""CREATE TABLE acc_data (
                    owner_id    INTEGER     NOT_NULL,
                    login       TEXT        NOT_NULL,
                    password    TEXT        NOT_NULL
                    )""")
    curs.execute("CREATE VIEW id_tech AS SELECT (COUNT(*) + 1) FROM accounts")
    conn.commit()

    acc_info = logging_in()


user_input = input('Press "1" to add password. Press "2" to retrieve your password: ')
if user_input == '1':
    add_password(acc_info)
elif user_input == '2':
    retrieve_password(acc_info)


# файлы должны браться *относительно* места, где они лежат?
# хранение информации в БД
# слон сдавайся\

