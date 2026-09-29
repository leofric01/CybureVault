import random
def check_password_strength():
    user_password=input(' Enter your Password ...:')
    if len(user_password) == 0: 
             print("You didn't enter anything!")
    elif len(user_password)<6:
        print(' pls sir make your password stronger than this ....')
    elif len(user_password)<=10:
        print(' hmm.. make it more strong pls ...')
    else:
        print(' its soo good mate ....')
def generate_password():
   chars="abcdefghijklmnopqrstuvwxyz1234567890"
   password = "".join(random.choices(chars, k=8))
   print('generated_password...: ', password)
def generate_username():
     name=input('Enter your Name sir....:')
     adj=random.choice(['cyber','dragon','teen','hollow','pretty lad'])
     number=random.randint(1, 100)
     print(name + '_' + str(number)+'_'+adj)
def validate_ip():
    ip=input(' Enter your Ip pls...:')
    parts=ip.split('.')
    if len(parts) == 4:
        print("Valid format!")
    else:
        print("Invalid IP address!")
def check_port():
     port=int(input(' Enter your port_number here ....:'))
     if port ==22:
          print(' its SSH')
     elif port ==80:
          print(' its HTTP')
     elif port ==443:
          print(' its HTTPS')
     else:
          print(' Unknown or custom port')
def caesar_cipher():
    text = input("Enter password to encrypt: ")
    encrypted = ""
    
    for char in text:
        encrypted += str(ord(char)) + "-"
        
    print("Encrypted numbers:", encrypted)