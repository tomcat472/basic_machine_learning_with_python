"""
procedural programming (PP) - function calling functions
object-oriented programming (OOP) - classes and objects
functional programming (FP) - passing functions to funtions
"""


# class Person:
#     def eat(self):
#         print("I am eating!")
#     def talk(self):
#         print("Hello!")

# def main():
#     person1=Person()
#     person2=Person()
    
#     person1.talk()
#     person2.eat()

# main()
# __________________________________________________________________
# class Person:
#     def __init__(self):
#         print("Person created")
    
#     def eat(self):
#         print("I am eating")
        
#     def talk(self):
#         print("Hello")
        
# def main():
#     person1=Person()
#     person2=Person()
    
#     person1.talk()
#     person2.eat()

# main()
# __________________________________________________________________
# class Person:
#     def __init__(self,name):
#         print(f"{name} created")
    
#     def eat(self):
#         print("I am eating")
        
#     def talk(self):
#         print("Hello")
        
# def main():
#     person1=Person("Tom")
#     person2=Person("SV")
    
#     person1.talk()
#     person2.eat()
    
# main()
# __________________________________________________________________
# class Person:
#     def __init__(self,name):
#         print(id(self))
#         print(f"{name} created")
    
#     def eat(self):
#         print("I am eating")
        
#     def talk(self):
#         print("Hello")
        
# def main():
#     person1=Person("Tom")
#     person2=Person("SV")
#     person3=Person("Pi")
    
#     person1.talk()
#     person2.eat()
    
#     print(id(person1))
#     print(id(person2))
#     print(id(person3))
    
# main()
# __________________________________________________________________
# class Person:
#     def __init__(self,name):
#         print(f"{name} created")
    
#     def eat(self):
#         print("I am eating")
        
#     def talk(self):
#         print("Hello")
        
# def main():
#     person1=Person("Tom")
#     person2=Person("SV")
    
#     person1.talk()
#     person2.eat()
    
#     person1.age=21
#     person2.age=42
    
#     print(person1.age)    
#     print(person2.age)
# main()
# _____________________________________________________________________________
# class Person:
#     def __init__(self,name):
#         # self.name=name
#         self._name=name
#         print(f"{self._name} created")
#         # print(f"{self.name} created")
        
#     def eat(self):
#         print("I am eating")
        
#     def talk(self):
#         print("Hello")
        
# def main():
#     person1=Person("Tom")
#     person2=Person("SV")
    
#     person1.talk()
#     person2.eat()
    
#     person1.age=21
#     person2.age=42
    
#     print(person1.age)    
#     print(person2.age)
# main()
# _________________________________________________________________________
# encapsulation
# class Cat:
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight
        
#     def __str__(self):
#         return f"Hello my name is {self.name},\nI weigh {self.weight:.1f}"
    
#     def introduce(self):
#         print(f"Hello my name is {self.name}, I weigh {self.weight:.1f}")
    
# def main():
#     cat1=Cat("tomas",1.43)
#     cat2=Cat("jack",1.264)

#     cat1.introduce()
#     cat2.introduce()
#     print(str(cat1))
    
#     cat2=str(cat2)
#     print(cat2)
# main()
# __________________________________________________________