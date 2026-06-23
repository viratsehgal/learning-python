while True:
    user_password = (input("Enter your password: "))
    errors = []

    if len(user_password) < 8:
        errors.append("Must be at least 8 characters long")
    if not any(char.isdigit() for char in user_password):
        errors.append("Must have at least 1 digit")
    if not any(char.isupper() for char in user_password):
        errors.append("Must have at least 1 uppercase letter")
    
    if errors:
        print("Password rejected. Failed rules:")
        for e in errors:
            print(e)
    else:
        print("Password accepted!!")
        break