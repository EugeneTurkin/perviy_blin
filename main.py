import os
import password_manager


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



if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users')):
    print("Welcome to Gill Bates' Password Manager! Please, create an account by following the instructions.")
    os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users'))
    acc_info = logging_in()
else:
    print('Welcome back!')
    acc_info = logging_in()


password_manager.manager(acc_info)


# файлы должны браться *относительно* места, где они лежат?
# хранение информации в БД
# слон сдавайся\

