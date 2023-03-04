import string
import random

#this program generates a random strong password

def generate_password(characters):
    password_length = int(input("How long would you like your password to be?  "))
    random.shuffle(characters)
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    return ("").join(password)


def main():
    print("Welcome to the password generator! ")
    #the characters we want to generate a password from
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    while True:
        option = input("Do you want to generate a password(yes/no) ")
        if option == 'yes':
            password = generate_password(characters)
            print(f"your new password is {password}")
        else:
            print('Program Terminated')
            break


main()