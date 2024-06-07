# value=False
# print(value)
# print(type(value))

# print("hello"=="Hello")

# is_equal = "hello" == "hello"
# print(is_equal)
# print(type(is_equal))
# ___________________________________________________________________________________

# name=input('enter your name: ')
# if name=="tom":
#     print("your name is tom")
#     print(f'Hello {name}')
# else:
#     print("your name isn't correct.")
# print("program finsihed")
# ______________________________________________________________________________________
# Name="herry"
# name=input('enter your name: ')
# if name==Name:
#     print(f"your name is {name}")
#     print(f'Hello {name}')
# else:
#     print("your name isn't correct.")
# print("program finsihed")
# __________________________________________________________________________________________
# stu1="tom"
# stu2="jame"
# stu3="herry"
# stu_name=input('enter your name: ')
# if stu_name==stu1:
#     print("enter room A")
# elif stu_name==stu2:
#     print("enter room b")
# elif stu_name==stu3:
#     print("enter room C")
# else:
#     print("go to room D")
# print('program finsihed')
# __________________________________________________________________________________________
# print('cat'=='dog')
# print(5==6)

# print(5<6)
# print(5>6)

# print("cat">"dog")
# print("cat" > "Dog")

# print(ord("C"),ord("D"),ord('c'),ord('d'))

# print('cat' != 'dig')

# print(4>=5)
# print(3<=32)
# _________________________________________________________________________________________
### Exercise
## < 0 - fridge (too cold), 0-4 "fridge ok", 4-6 "fridge too warm", >6- "fridge broken"

# temp=float(input("input fridge temperature "))
# if temp<0:
#     print("frigde is too cold.")
# elif temp<=4:
#     print("fridge is ok")
# elif temp < 6:
#     print("fridge is too warm")
# else:
#     print("fridge is broken.")
# ______________________________________________________________________________
# temp=float(input("enter temperature of fridge "))

# status_broken="fridge is broken"
# status_ok="fridge ok"
# status_cold="fridge is too cold"
# status_warm="fridge is too warm"
# status=status_broken

# if temp<0:
#     status=status_cold
# elif temp<=4:
#     status=status_ok
# elif temp<6:
#     status=status_warm
# print(status)
# ___________________________________________________________________________________
# for i in range(5):
#     print(str(i)+" Hello")
    
# for i in range(0,10,2):
#     print(i)

# for _ in range(4):
#     print("hi")
# ____________________________________________________________________________________

# for i in range(5,8):
#     print(i)
#     if i == 6:
#         print("6 is here")

# _____________________________________________________________________________________
# for i in range(5):
#     print("loop number is "+str(i))
    
#     stop=input("stop the loop (y/n) ?")
#     if stop=="y":
#         # break
#         print("relax")
#         continue
#     print("ending loop number is "+str(i))
# print("programm finished")
# ______________________________________________________________________________________
# password="123456"
# for _ in range(3):
#     user_password=input('Enter your password: ')
    
#     if user_password == password:
#         print("Welcome to home")
#         break
#     else:
#         print("access denied")
# ________________________________________________________________________________________
# password="123456"
# correct=False
# for _ in range(3):
#     user_password=input("Enter your password: ")
    
#     if password==user_password:
#         correct=True
#         if correct:
#             print("Welcome to home")
#         break
#     else:
        # print("incorrect password")
# _______________________________________________________________________________________
# print(23>324 and 324<230)
# print(32<323 | 32>333)
# print(not(324>3))
# ______________________________________________________________________________________
# student=input('are you a student? (y/n): ')
# pets=input("do you have any pets? (y/n): ")
# smokes=input("do you smoke? (y/n): ")

# is_student=student=="y"
# has_pets=pets=="y"
# does_smoke=smokes=="y"

## print(is_student,has_pets,does_smoke)

# student_can_rent=is_student and not has_pets and not does_smoke
# non_student_can_rent= not is_student and not (does_smoke and has_pets)
## print(student_can_rent)
## print(non_student_can_rent)

# can_rent=student_can_rent or non_student_can_rent
# print("Can rent: "+str(can_rent))
# ______________________________________________________________________________________
# student=input('are you a student? (y/n): ')
# pets=input("do you have any pets? (y/n): ")
# smokes=input("do you smoke? (y/n): ")

# is_student=student=="y"
# has_pets=pets=="y"
# does_smoke=smokes=="y"

# can_rent=False
# if is_student:
#     if does_smoke or has_pets:
#         can_rent=False
#     else:
#         can_rent=True
# else:
#     if does_smoke and has_pets:
#         can_rent=False
#     else:
#         can_rent=True
# print("can rent: "+str(can_rent))
# ____________________________________________________________________________
password="123456"
user_password=""
while user_password != password:
    user_password=input("enter your password! ")
print("access granted")