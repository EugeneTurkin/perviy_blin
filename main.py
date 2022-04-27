import os
import password_manager


def logging_in():
    login = input('Enter your login: ')
    password = input('Enter your password: ')
    return f'{login},{password}'


if os.path.exists(os.getcwd() + '\\users'):
    print('Welcome back!')
    acc_info = logging_in()
    if acc_info not in os.listdir(os.getcwd() + '\\users'):
        input('This account does not exist. Creating a new one.')
        os.makedirs(f'users\\{acc_info}')
else:
    print("Welcome to Gill Bates' Password Manager! Please, create an account by following the instructions.")
    acc_info = logging_in()
    os.makedirs(f'users\\{acc_info}')

os.chdir(f'users\\{acc_info}')
password_manager.manager(acc_info)


# файлы должны браться *относительно* места, где они лежат?
# хранение информации в БД

