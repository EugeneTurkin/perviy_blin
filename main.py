import password_manager

from pathlib import Path


users_dir = Path(__file__).parent / "users"


if not users_dir.exists():
    users_dir.mkdir()
    print("Welcome to Gill Bates' Password Manager! Please, create an account by following the instructions.")
    acc_info = password_manager.logging_in()
else:
    print('Welcome back!')
    acc_info = password_manager.logging_in()


user_input = input('Press "1" to add password. Press "2" to retrieve your password: ')
if user_input == '1':
    password_manager.add_password(acc_info)
elif user_input == '2':
    password_manager.retrieve_password(acc_info)
