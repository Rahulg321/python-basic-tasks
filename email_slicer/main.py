#takes an email and slices it into username, domain and extension
#collect email from user
#slice and split using the @


def main():
    print('welcome to the email slicer')
    print()
    email_input = input('Enter your email address: ')
    
    user_name,domain = email_input.split('@')
    domain,extension = domain.split('.')
    
    print(f'username = {user_name}')
    print(f'domain = {domain}')
    print(f'extension = {extension}')
    print()
    
  
while True:   
    main()