"""
function main()
  get password
  print_asterisk(password)

function get_password()
  get user_password
  while len(user_password) < PASSWORD_LENGTH
    display "Error! Enter minimum a {PASSWORD_LENGTH} digit password"
    get user_password
  return len(user_password)

function print_asterisk(user_password)
  display ("*" * user_password)
"""

PASSWORD_LENGTH = 4


def main():
    password = get_password()
    print_asterisk(password)


def get_password():
    user_password = input("Enter password: ")
    while len(user_password) < PASSWORD_LENGTH:
        print(f"Error! Enter minimum a {PASSWORD_LENGTH} digit password")
        user_password = input("Enter password:")
    return len(user_password)


def print_asterisk(user_password):
    print("*" * user_password)


main()
