import re

realapplication)
password_history = set()

def is_password_strong(password):

    if len(password) < 8:
        return False


    if not any(char.isupper() for char in password):
        return False


    if not any(char.islower() for char in password):
        return False


    if not any(char.isdigit() for char in password):
        return False


    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False


    if password in password_history:
        return False

    return True

def main():
    while True:
        password = input("Enter a new password: ")
        if is_password_strong(password):
            print("Password is strong and accepted.")

            password_history.add(password)
            break
        else:
            print("Password does not meet the criteria. Try again.")

if __name__ == "__main__":
    main()
