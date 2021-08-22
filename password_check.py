trigger = False

while not trigger:
    user_password = input("Enter password: ")
    length = len(user_password)
    if length >= 5:
        trigger = True
        print("*" * length)
    else:
        print("Password must be more than 4 characters")