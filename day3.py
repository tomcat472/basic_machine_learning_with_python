# def ask_user_status():
#     response=input("How are you?: ")
    
#     if response=="Ok" or response=="ok":
#         print("excellent")
#     else:
#         print("no")
        
# ask_user_status()
# __________________________________________________________________
# password="Hello"
# def greeting():
#     print("Welcome! No unauthorised users")
    
# def check_password():
#     user_password=input("Enter your password: ")
    
#     if password == user_password:
#         print("access granted")
#     else:
#         print("access denied")
        
# def main():
#     greeting()
#     check_password()

# main()
# ______________________________________________________________________________
# def greet(name):
#     print(id(name))
#     print(f"Hello {name}")
    
# def main():
#     name="Tom"
#     print(id(name))
#     greet(name)
    
# main()
# _______________________________________________________________________________
# def greet(name):
#     print("Hello "+name)
#     print("1. value of name is greet is: "+name)
#     name="Jame"
#     print("2. value of name in greet is ",name)
    
# def main():
#     name="John"
#     print("1. value of name in main is "+name)
#     greet(name)
#     print("2. value of name in main is "+name)

# main()
# _____________________________________________________________________________________
# def greet(name):
#     print(f"Hello {name}")

# def creating_greeting(name):
#     return f"Hi {name}"

# def create_simple_greeting():
#     return "Hi there"

# def main():
#     name="John"
#     greet(name)
    
#     greeting=creating_greeting(name)
#     print(greeting)
    
#     simple_greeting=create_simple_greeting()
#     print(simple_greeting)
    
# main()
# ___________________________________________________________________________________
def calculate_box_volume(width,height,length):
    return width * height * length

def main():
    volume=calculate_box_volume(12,3,22)
    print(f"Box volume is {volume}")

main()
