from rot import rot13
import os
from pathlib import Path


users_dir = Path(__file__).parent / "users"


class User():
    def __init__(self, email, password):
        self.email = email
        self.password = password


def logging_in():
    login = input('Enter your login: ')
    password = input('Enter your password: ')

    user_data_file = users_dir / f"{login},{password}.txt"
    if not user_data_file.exists():
        with open(user_data_file, "w"):
            pass
        print('This account does not exist. A new one was created.')

    return User(login, password)


def add_password(acc_info):
    user_email = input('Enter your e-mail: ')
    user_password = input('Enter your password: ')

    user_data_file = users_dir / f"{acc_info.email},{acc_info.password}.txt"
    with user_data_file.open('a') as f:
        f.write(f'{user_email},{rot13(user_password)}\n')
    print('Password is saved successfully')


def retrieve_password(acc_info):
    user_email = input('Enter your e-mail: ')

    user_data_file = users_dir / f"{acc_info.email},{acc_info.password}.txt"
    with user_data_file.open('r') as f:
        for line in f:
            if user_email in line:
                _, _, user_password = line.partition(',')
                print(f'Your password is: {rot13(user_password)}')
                break
