# import random

# def main():
#     pets=["dog","cat","rabbit"]
#     pet=random.choice(pets)
#     print(pet)
    
    
#     print()
#     print()
#     for i in range(0,30):
#         animal=pets[i%len(pets)]
#         print(animal,end=", ")
# main()
# ____________________________________________________________
# def main():
#     print("Hello "+"there")
#     print("Hello "+str(7))
#     print("Hello",100,{1,2,3},1.23)
    
#     print("hello".upper())
#     print("HeLLo".casefold())
#     print(", ".join({'one',"two","three"}))
#     print("Hello",end="...")
#     print("Hi")
    
#     print("Hi,\nhow are you")    
#     print()
#     print("Hi,\nhow\nare\tyou\\")
#     print('"Hello"')
#     print("'Hi")
#     print("Hello \"Bob\"")
# main()
# ____________________________________________________________
# def main():
#     name="Zoe"
#     text="Hello %s. how are you?" % name
#     print(text)
    
#     print("Hello %s and %s. How are you today?" % ("Jack","Morty"))
#     print("Hello %s. The temperature is %d"%("Zoe",31))
#     print("Hello %s. The temperature is %f"%("Morty",28.3233))
#     print("Hello %s. The temperature is %.2f"%("Morty",28.3233))
#     print("Hello %s. The temperature is %10d"%("Zoe",31))
#     print("Floating point in a width of 10: %10.1f"%1.24533)

# main()
# ____________________________________________________________
# def main():
#     print("Hello {}".format("Morty"))
#     print("Hello {1} and {0}".format("Summer","Morty"))
#     print("The temperature is {}".format(11))
#     print("The temperature is {:.2f}".format(12.2334))
#     print("We have {number_units} units avaiable".format(number_units=98))
#     print("Hello {name}.It is {temp:.1f} degree today".format(temp=23.32,name="Morty"))
#     print()
    
#     print("It is {dist:,.0f} mile to sun".format(dist=9.3E7))
#     print("Hello {:>20}".format("Morty"))
#     print("We have {:.1%} fuel left".format(0.25))
# main()
# ____________________________________________________________
# name="Morty"
# temp=34.23423
# greeting=f"Hello {name.upper()}, the temperature is {temp:.2f} C"
# print(greeting)
# ____________________________________________________________
path=r"C:\\Users\\Admin\\Desktop\\python_machine_learning\\env"
print(path)

print("Hello" 'World')