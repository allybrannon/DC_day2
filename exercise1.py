# Create a program that will ask for a username and then a password.
# If the username or password length is less than 6 charecters give a too short message.
# if the username or password length is greater than 12 charecters give a too long message
# Have the user confirm the password in again.
# If the passwords match give a sucess message
# if the passwords do not match give a mismatch message
# If the password is only numbers give a message that says it cannot be a number.
# (challange) have only one print statement in the whole program.

user_name = input("What is your username?\n")
password = input("What is your password?\n")

if len(user_name) < 6 or len(password) < 6:
    print("Length is too short!")
elif len(user_name) > 12 or len(password) > 12:
    print("Length is too long!")

confirm_password = input("Confirm password!\n")

if confirm_password == password:
    if confirm_password.isdigit():
        print("Fail!")
    else:
        print("Success!")


else:
    print("Fail! Passwords do not match!")
