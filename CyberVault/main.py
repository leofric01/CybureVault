from tools import check_password_strength
from tools import generate_password
from tools import generate_username
from tools import validate_ip
from tools import check_port
from tools import caesar_cipher 
print(' greetings sir its your Cyber system ')
user_name=input(' Enter your name : ')
user_age=int(input('Enter your age sir :'))
if user_age>=18:
    print(' HEllo sir you can use me all the time ...... ')
    user_email=input('pls Sir Enter your Email here .... :')
    user_password=input('pls Sir Enter your Password here .... :')
    user_data = {
    "name": user_name,
    "email": user_email,
    "password": user_password,
    }
if user_age<18:
    print(' Sorry Sir not yet ')
    exit()
while True:
 print('==================================')
 print('       CYBERVAULT DASHBOARD       ')
 print('==================================')
 print("[1] Password Strength Checker")
 print("[2] Password Generator")
 print("[3] Username Generator")
 print("[4] IP Address Validator")
 print("[5] Port Checker")
 print("[6] Caesar Cipher")
 print("[7] View Activity Log")
 print("[0] Exit")
 choice = input("Enter your choice (0-7): ")
 if choice =='0':
    print('Thank you sir for using me')
    exit()
 if choice =='1':
    print('Loading Password Strength Checker...')
    check_password_strength()
 elif choice == '2':
        print('Loading Password Generator...')
        generate_password()
 elif choice == '3':
        print('Loading Username Generator...')
        generate_username()
 elif choice == '4':
        print('Loading IP Address Validator...')
        validate_ip()
 elif choice == '5':
        print('Loading Port Checker...')
        check_port
 elif choice == '6':
        print('Loading Caesar Cipher...')
        caesar_cipher
else:
        print('Invalid choice, please select between 0 and 7!')