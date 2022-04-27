from rot import rot13


def manager(acc_info):
    user_input = input('Press "1" to add password. Press "2" to retrieve your password: ')
    if user_input == '1':
        user_email = input('Enter your e-mail: ')
        user_password = input('Enter your password: ')
        with open(f'{acc_info}.txt', 'a') as f:
            f.write(f'{user_email},{rot13(user_password)}\n')
        print('Password is saved successfully')
    elif user_input == '2':
        user_email = input('Enter your e-mail: ')
        with open(f'{acc_info}.txt', 'r') as f:
            for line in f:
                if user_email in line:
                    _, _, user_password = line.partition(',')
                    print(f'Your password is: {rot13(user_password)}')
                    break
    else:
        print("something went wrong. Try again.")
        manager()

