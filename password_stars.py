minimum_set_length = 4
user_password = input("Enter password:")
while len(user_password) < minimum_set_length:
    print(f"Error! Enter minimum a {minimum_set_length} digit password")
    user_password = input("Enter password:")
print("*" * len(user_password))
