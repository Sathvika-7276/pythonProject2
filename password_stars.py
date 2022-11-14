minimum_set_length = 4


def get_password():
    user_password = input("Enter password:")
    while len(user_password) < minimum_set_length:
        print(f"Error! Enter minimum a {minimum_set_length} digit password")
        user_password = input("Enter password:")
    print_asterisk(user_password)


def print_asterisk(user_password):
    print("*" * len(user_password))


get_password()
