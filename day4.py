# def factorial(value):
#     result=1
    
#     for i in range(2,value+1):
#         result=result*i
#     return result

# def main():
#     result=factorial(5)
    
#     print(f'factorial result is {result}')

# main()
# ________________________________________________________________
## default arguments
# def student(name,room="A",age=18):
#     print(name,room,age)
    
# def main():
#     student("Mg Mg","A",21)
#     student("Hla Hla")
#     student("Aung Aung",age=20)
#     student("Ko Ko",room="D")
# main()
# __________________________________________________________________
## keyword arguments
# def fruit(color,weight,sweetness,location):
#     print(color)
#     print(weight)
#     print(sweetness)
#     print(location)
    
# def main():
#     fruit("red",1,50,"colombia")
#     print()
#     fruit(color="brown",sweetness=60,weight=0.5,location="thailand")

# main()
# _____________________________________________________________
## variable length arguments
# def describe_people(name,*attribute):
#     print(name)
#     for attr in attribute:
#         print(attr)
        
# def main():
#     describe_people("Aung Aung","warm","smart","funny")
#     print()
#     describe_people("Hla Hla")
#     print()
#     describe_people("Ma Ma","beautiful","bright")
# main()
# ___________________________________________________________________
## variable length keyword arguments
# def add_description(**kwargs):
#     # print(type(kwargs))
#     # print(kwargs)
#     # for a,b in kwargs.items():
#     #     print(a,":",b)
#     for a in kwargs:
#         print(a,":",kwargs[a])
#     print()
    
# def main():
#     add_description(apple="red",price=1000)
#     add_description(sex="male",height=190,town="mdy")

# main()
# ________________________________________________________________
## arguments and parameters summary
# def positional_arguments(one,two,three):
#     print(one)
#     print(two)
#     print(three)
    
# def default_argument(one,two=2,three=3):
#     print(one)
#     print(two)
#     print(three)

# def variable_arguments(*args):
#     for arg in args:
#         print(arg)

# def variable_keyword_arguments(**kwargs):
#     for key in kwargs:
#         print(key,'-----',str(kwargs[key]))
# def main():
#     # 1. positional arguments
#     positional_arguments(1,2,3)
#     print()
    
#     # 2.default argumnets
#     default_argument(2)
#     print()
    
#     # 3. keyword arguments
#     positional_arguments(one="Hello",two="there",three="friend")
#     print()
    
#     # 4. variable arguments
#     variable_arguments("orange","banana","grape",1,2,3)
#     print()
    
#     # 5. variable keyword arguments
#     variable_keyword_arguments(speed=90,color='brown',size='big')
#     print()

# main()
# _________________________________________________________________
# def test(name,*args,**kwargs):
#     print(name)
#     print()
    
#     for arg in args:
#         print(arg)
#     print()
    
#     for key in kwargs:
#         print(key,":",kwargs[key])
#     print()

# def main():
#     test('apple','orange',23,3,apple=500,lime=50)

# main()
# ______________________________________________________________
# # multi return values
# def get_user_info():
#     name=input('Enter your name --> ')
#     height=input('Enter your height --> ')
    
#     return name, height

# def main():
#     name,height=get_user_info()
#     print(name+'----->'+height)
# main()
# _______________________________________________________________
## Bmi exercise
def calculate_bmi():
    weight=input('enter your weight in kilos: ')
    height=input('enter your height in meters: ')
    
    weight=float(weight)
    height=float(height)
    
    bmi=weight/ (height*height)
    return weight, height, bmi

def main():
    weight,height,bmi=calculate_bmi()
    print("Weight: ",weight)
    print("Height: ", height)
    print("BMI: ",bmi)

main()