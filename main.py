import os
import password_manager


if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users')):
    print("Welcome to Gill Bates' Password Manager! Please, create an account by following the instructions.")
    os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users'))
    acc_info = password_manager.logging_in()
else:
    print('Welcome back!')
    acc_info = password_manager.logging_in()


user_input = input('Press "1" to add password. Press "2" to retrieve your password: ')
if user_input == '1':
    password_manager.add_password(acc_info)
elif user_input == '2':
    password_manager.retrieve_password(acc_info)


# файлы должны браться *относительно* места, где они лежат?
# хранение информации в БД
# слон сдавайся\

