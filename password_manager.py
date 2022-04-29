from rot import rot13
import os


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


def manager(acc_info):
    user_input = input('Press "1" to add password. Press "2" to retrieve your password: ')
    if user_input == '1':
        add_password(acc_info)
    elif user_input == '2':
        retrieve_password(acc_info)

