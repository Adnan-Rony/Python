password = input("Enter a password: ")

if len(password) >= 8 and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in "@#$%" for c in password):
    print("Password is strong:", password)
else:
    print("Something is wrong with the password. Please make sure it meets all the criteria.")
