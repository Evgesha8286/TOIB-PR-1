def check_password(password):
    upper_set = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lower_set = set('abcdefghijklmnopqrstuvwxyz')
    digit_set = set('1234567890')
    spec_set = set('!@#$%&')
    value = True
    # Длина строки пароля восемь символов.
    if len(password) != 8:
        print('Длинна пароля должна составлять 8 символов')
        value = False
    if not any(char in upper_set for char in password):
        print('В пароле нет заглавных символов')
        value = False
    if not any(char in lower_set for char in password):
        print('В пароле нет прописных символов')
        value = False
    if not any(char in digit_set for char in password):
        print('В пароле нет цифр')
        value = False
    if not any(char in spec_set for char in password):
        print('В пароле нет специальных символов')
        value = False
    if value:
        return value
def main():
    print ("Введите пароль:")
    password = input()
    if (check_password(password)):
        print("Действительный пароль")
    else:
        print("Пароль не соответствует требованиям")
if __name__ == '__main__':
    main()