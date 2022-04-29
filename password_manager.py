from rot import rot13
import os


class User():
    def __init__(self, email, password):
        self.email = email
        self.password = password


def logging_in():
    login = input('Enter your login: ')
    password = input('Enter your password: ')
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users'))
    if '{},{}.txt'.format(login, password) not in os.listdir(os.getcwd()):
        print('This account does not exist. A new one was created.')
    with open('{},{}.txt'.format(login, password), 'a'):
        pass
    return User(login, password)


def add_password(acc_info):
    user_email = input('Enter your e-mail: ')
    user_password = input('Enter your password: ')
    with open('{},{}.txt'.format(acc_info.email, acc_info.password), 'a') as f:
        f.write(f'{user_email},{rot13(user_password)}\n')
    print('Password is saved successfully')


def retrieve_password(acc_info):
    user_email = input('Enter your e-mail: ')
    with open('{},{}.txt'.format(acc_info.email, acc_info.password), 'r') as f:
        for line in f:
            if user_email in line:
                _, _, user_password = line.partition(',')
                print(f'Your password is: {rot13(user_password)}')
                break




